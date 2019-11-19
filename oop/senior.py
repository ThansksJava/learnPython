class Student:
    # __slots__ limit the attr that one obj enable to add
    # __slots__ only affects itself unless its children also define __slot__ attr
    __slots__ = ('name', 'age')


s = Student()
s.name = 'Michael'
s.age = 25
# so adding score addr is disabled
# s.score = 99





