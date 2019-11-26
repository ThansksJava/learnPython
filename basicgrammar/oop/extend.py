class Animal(object):
    def run(self):
        print(self.__class__.__name__, ' is running...')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
dog.run()

cat = Cat()
cat.run()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(dog, Cat))


class Plant:
    def run(self):
        print('Start...')


t = Plant()

print(isinstance(t,Animal))


print("type dog", type(dog))
print("type cat", type(cat))
print("type cat", type(t))


print("dir dog", dir(dog))
