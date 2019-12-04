import unittest

# from . import Class
# from . import Instance
# from . import Base
# from . Instance import OBJECT
# from . Instance import TYPE
from FhLinesorLess.A_Simple_Object_Model.Class import Class
from FhLinesorLess.A_Simple_Object_Model.Instance import Instance
from FhLinesorLess.A_Simple_Object_Model.Instance import OBJECT
from FhLinesorLess.A_Simple_Object_Model.Instance import TYPE


class TestOO(unittest.TestCase):
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
        assert  b.isinstance(B)
        assert b.isinstance(A)
        assert b.isinstance(OBJECT)
        assert not b.isinstance(TYPE)
