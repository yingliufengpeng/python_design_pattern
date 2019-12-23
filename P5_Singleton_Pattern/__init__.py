

class Single(object):

    instance = None

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):

        if cls.instance:
            return cls.instance

        obj = object.__new__(cls)

        cls.instance = obj

        return obj

a = Single('w')

b = Single('p')

print(a)
print(b)




