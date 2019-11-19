class Chain:
    def __init__(self, path=""):
        self._path = path

    def __getattr__(self, path):
        # "%s/%s" % (self._path, path) means use the word after %  replace %s
        return Chain("%s/%s" % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


url = Chain().status.user.timeline.list

print(url)
