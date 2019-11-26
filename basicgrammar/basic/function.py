import math

# function
print("=======start====function")
# help(abs)
print(abs(-100))
print(hex(100))


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(100))
print(my_abs(-100))


# define a function which use functions in package math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
