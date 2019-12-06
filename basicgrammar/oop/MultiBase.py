class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print('Hi, my value is', self.value)


class TalkingCalculator(Calculator, Talker):
    pass


c = TalkingCalculator()
c.calculate("18")
c.talk()

print(hasattr(c,"talk"))