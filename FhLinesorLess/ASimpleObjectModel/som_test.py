from unittest import TestCase
from FhLinesorLess.ASimpleObjectModel.Class import Class
from FhLinesorLess.ASimpleObjectModel.Instance import OBJECT, TYPE, Instance


class OO(TestCase):
    def test_isinstance(self):
        # Python code
        class A(object):
            pass

        class B(A):
            pass

        b = B()
        assert isinstance(b, B)
        assert isinstance(b, A)
        assert isinstance(b, object)
        assert not isinstance(b, type)
        # Object model code
        A = Class(name="A", base_class=OBJECT, fields={}, metaclass=TYPE)
        B = Class(name="B", base_class=A, fields={}, metaclass=TYPE)
        b = Instance(B)
        assert b.isinstance(B)
        assert b.isinstance(A)
        assert b.isinstance(OBJECT)
        assert not b.isinstance(TYPE)

    def test_callmethod_subclassing_and_arguments(self):
        # Python code
        class A(object):
            def g(self, arg):
                return self.x + arg

        obj = A()
        obj.x = 1
        assert obj.g(4) == 5

        class B(A):
            def g(self, arg):
                return self.x + arg * 2

        obj = B()
        obj.x = 4
        assert obj.g(4) == 12

        # Object model code
        def g_A(self, arg):
            return self.read_attr("x") + arg

        A = Class(name="A", base_class=OBJECT, fields={"g": g_A}, metaclass=TYPE)
        obj = Instance(A)
        obj.write_attr("x", 1)
        assert obj.callmethod("g", 4) == 5

        def g_B(self, arg):
            return self.read_attr("x") + arg * 2

        B = Class(name="B", base_class=A, fields={"g": g_B}, metaclass=TYPE)
        obj = Instance(B)
        obj.write_attr("x", 4)
        assert obj.callmethod("g", 4) == 12

    def test_getattr(self):
        # Python code
        class A(object):
            def __getattr__(self, name):
                if name == "fahrenheit":
                    return self.celsius * 9. / 5. + 32
                raise AttributeError(name)

            def __setattr__(self, name, value):
                if name == "fahrenheit":
                    self.celsius = (value - 32) * 5. / 9.
                else:
                    # call the base implementation
                    object.__setattr__(self, name, value)

        obj = A()
        obj.celsius = 30
        assert obj.fahrenheit == 86  # test __getattr__
        obj.celsius = 40
        assert obj.fahrenheit == 104

        obj.fahrenheit = 86  # test __setattr__
        assert obj.celsius == 30
        assert obj.fahrenheit == 86

        # Object model code
        def __getattr__(self, name):
            if name == "fahrenheit":
                return self.read_attr("celsius") * 9. / 5. + 32
            raise AttributeError(name)

        def __setattr__(self, name, value):
            if name == "fahrenheit":
                self.write_attr("celsius", (value - 32) * 5. / 9.)
            else:
                # call the base implementation
                OBJECT.read_attr("__setattr__")(self, name, value)

        A = Class(name="A", base_class=OBJECT,
                  fields={"__getattr__": __getattr__, "__setattr__": __setattr__},
                  metaclass=TYPE)
        obj = Instance(A)
        obj.write_attr("celsius", 30)
        assert obj.read_attr("fahrenheit") == 86  # test __getattr__
        obj.write_attr("celsius", 40)
        assert obj.read_attr("fahrenheit") == 104
        obj.write_attr("fahrenheit", 86)  # test __setattr__
        assert obj.read_attr("celsius") == 30
        assert obj.read_attr("fahrenheit") == 86

    def test_get(self):
        # Python code
        class FahrenheitGetter(object):
            def __get__(self, inst, cls):
                return inst.celsius * 9. / 5. + 32

        class A(object):
            fahrenheit = FahrenheitGetter()

        obj = A()
        obj.celsius = 30
        assert obj.fahrenheit == 86

        # Object model code
        class FahrenheitGetter(object):
            def __get__(self, inst, cls):
                return inst.read_attr("celsius") * 9. / 5. + 32

        A = Class(name="A", base_class=OBJECT,
                  fields={"fahrenheit": FahrenheitGetter()},
                  metaclass=TYPE)
        obj = Instance(A)
        obj.write_attr("celsius", 30)
        assert obj.read_attr("fahrenheit") == 86

    def test_maps(self):
        # white box test inspecting the implementation
        Point = Class(name="Point", base_class=OBJECT, fields={}, metaclass=TYPE)
        p1 = Instance(Point)
        p1.write_attr("x", 1)
        p1.write_attr("y", 2)
        assert p1.storage == [1, 2]
        assert p1.map.attrs == {"x": 0, "y": 1}

        p2 = Instance(Point)
        p2.write_attr("x", 5)
        p2.write_attr("y", 6)
        assert p1.map is p2.map
        assert p2.storage == [5, 6]

        p1.write_attr("x", -1)
        p1.write_attr("y", -2)
        assert p1.map is p2.map
        assert p1.storage == [-1, -2]

        p3 = Instance(Point)
        p3.write_attr("x", 100)
        p3.write_attr("z", -343)
        assert p3.map is not p1.map
        assert p3.map.attrs == {"x": 0, "z": 1}
