import pickle

d = dict(name="冯杰", age=26, score=100)

s = pickle.dumps(d)

with open("D:/serialization", 'wb') as f:
    f.write(s)


with open("D:/serialization", 'rb') as f:
    # sd = f.readline()
    # print(sd)
    d = pickle.load(f)
    print(d)
