def f(x):
    return x * x


r = map(f, list(range(1, 10)))
print(list(r))


def normalize(names):
    i = 0
    for name in names:
        print(name)
        names[i] = name.title()
        i += 1
    print(names)


normalize(['adam', 'LISA', 'barT'])

