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

if __name__=='__main__':
    TestCase