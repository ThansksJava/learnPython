# return function
def create_counter():
    def plus():
        n = 0
        while True:
            n = n + 1
            yield n

    x = plus()

    def counter():
        return next(x)

    return counter


create = create_counter()
print(create(), create(), create())
