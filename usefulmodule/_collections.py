from collections import namedtuple,deque,defaultdict,OrderedDict

# named tuple
print("========named tuple========")
Point = namedtuple("Point", ["X", "Y"])
p = Point(1,2)
print(p.X)
print(p.Y)
print("=====deque=======")
d = deque(["a", "b", "c"])
d.append("x")
d.append("y")
print(d)
print("=====defaultdict=======")
# notice : the default value is appointed by function
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

print("==========OrderedDict=========")
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)