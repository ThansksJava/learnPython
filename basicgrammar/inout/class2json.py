import json


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return self.name + ":" + str(self.age)

def student2dict(stu):
    return {
        "name": stu.name,
        "age": stu.age
    }


def dict2student(d):
    return Student(d['name'], d['age'])


s = Student("二哈", 22)

jsons = json.dumps(s, default=student2dict)

print(jsons)

st = json.loads(jsons,object_hook=dict2student)
print(st)
