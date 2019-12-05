from .Base import Base,MISSING
from .Class import Class


class Instance(Base):
    """Instance of a user-defined class. """

    # def __init__(self, cls):
    #     assert isinstance(cls, Class)
    #     Base.__init__(self, cls, {})
    def __init__(self, cls):
        assert isinstance(cls, Class)
        Base.__init__(self, cls, None)
        self.map = EMPTY_MAP
        self.storage = []

    def _read_dict(self, fieldname):
        # map store the name and index and array store the value
        index = self.map.get_index(fieldname)
        if index == -1:
            return MISSING
        return self.storage[index]

    def _write_dict(self, fieldname, value):
        index = self.map.get_index(fieldname)
        if index != -1:
            self.storage[index] = value
        else:
            new_map = self.map.next_map(fieldname)
            self.storage.append(value)
            self.map = new_map

def OBJECT__setattr__(self, fieldname, value):
    self._write_dict(fieldname, value)


class Map(object):
    def __init__(self, attrs):
        self.attrs = attrs
        self.next_maps = {}

    def get_index(self, fieldname):
        return self.attrs.get(fieldname, -1)

    def next_map(self, fieldname):
        assert fieldname not in self.attrs
        if fieldname in self.next_maps:
            return self.next_maps[fieldname]
        attrs = self.attrs.copy()
        attrs[fieldname] = len(attrs)
        result = self.next_maps[fieldname] = Map(attrs)
        return result


EMPTY_MAP = Map({})



OBJECT = Class("object", None, {"__setattr__": OBJECT__setattr__}, None)
TYPE = Class(name="type", base_class=OBJECT, fields={}, metaclass=None)
OBJECT.cls = TYPE
TYPE.cls = TYPE
