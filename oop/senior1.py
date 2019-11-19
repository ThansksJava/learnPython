class Student(object):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    def __len__(self):
        return len(self._name)

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


s = Student()
s.score = 60
s.name = "fengjie"
print("len(s)", len(s))
print(s.score)
print("Print Student:", s)


class Screen(object):
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, w):
        self.__width = w

    @height.setter
    def height(self, h):
        self.height = h

    @property
    def resolution(self):
        return self.height * self.width

    def __getattr__(self, item):
            return item + "属性不存在"


s = Screen()
print(s.age)
