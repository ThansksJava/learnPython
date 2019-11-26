from collections import Counter

c = Counter()

for x in "qwerqerqfdqqfqwtegfweqrfADEEQWGQWEF":
    c[x] = c[x] + 1

print(c)