# string to int
print(int('12345'))
print(int("123", base=8))
print(int('0x16', base=16))
print(int('12345', base=0))

print(int("10110", base=2))


def int2(x, base=2):
    return int(x, base)


print(int2('1111'))
