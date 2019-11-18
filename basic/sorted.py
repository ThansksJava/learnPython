s = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(s)

s1 = sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)
print(s1)


s2 = sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True)
print(s2)

CONST = {
    'a':1,
    'b':2
}


def by_name(t):
    return t[0]


L = [('Bob', 75), ('adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
print(L2)