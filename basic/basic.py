import os
# say hello to world
print("hello world")
# list's operation
classmate = ["michael", 'bob', 'jack']
print(len(classmate))
print(classmate)
print(classmate[1])
print(classmate[-1])

print("slice:", classmate[0:2])

classmate.append("xiaoming")
print(classmate[-1])
classmate.pop(-1)
print(classmate[-1])
classmate[1] = "longgang"
print(classmate)

classmate.append(["another class", "another class"])
print(classmate)
# tuple -- immutable sorted list
print("=======tuple start:inner member's pointer never change========")
tupleClassmate = ("1", "2", "3")
print(len(tupleClassmate))
# Traceback (most recent call last):
#   File "D:/workspace/learnPython/basic/basic.py", line 22, in <module>
#     tupleClassmate[1] = "111"
# TypeError: 'tuple' object does not support item assignment
# tupleClassmate[1] = "111"

# condition
print("======condition start =======")
age = 40
if age >= 18:
    print('your age is', age)
    print('adult')
if age >= 40:
    print("Middle-aged")
else:
    print("teenager")
s = 222
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

print("=====circular expression=====")
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
print("=====range to list expression=====")
rangToList = list(range(100))
print(rangToList)
print("=====dict also named as map in Java=====")
score = {"fengjie": 100,"other": 99}
for x in score:
    print(x)
    print(score[x])

print("=========iterate dic=========")
for k, v in score.items():
    print(k, ":", v)



# set
print("=========set start=======")
s = set([1, 2, 3])
print(s)
s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s1.add(4)
print(s1)
# remove(key)
s1.remove(1)
print(s1)

# List Comprehensions
print("======List Comprehensions========")
l1 = list(x * x for x in range(1, 11))
print(l1)

l2 = list(d for d in os.listdir("."))
print(l2)




print("  ")
print("  ")
print("  ")
print("  ")
print("  ")
print("  ")
print("  ")
print("  ")