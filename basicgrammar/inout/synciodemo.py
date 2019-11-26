path = r'C:\Windows\system.ini'

with open(path, 'r') as f:
    for s in f.readlines():
        print(s)
