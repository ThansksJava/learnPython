from .Base import Base
from .Class import Class


class Instance(Base):
    """Instance of a user-defined class. """

    def __init__(self, cls):
        assert isinstance(cls, Class)
        Base.__init__(self, cls, {})


OBJECT = Class(name="object", base_class=None, fields={}, metaclass=None)
TYPE = Class(name="type", base_class=OBJECT, fields={}, metaclass=None)
OBJECT.cls = TYPE
TYPE.cls = TYPE
