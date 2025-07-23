import pdb
class Meta(type):
    def __new__(cls, name, bases, dct):
        print("Meta.__new__ called")
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print("Meta.__init__ called")
        cls.calls = 0 #controls the number of distinct object instances
        cls.data = None

        super().__init__(name, bases, dct)

    def __call__(cls, *args, **kwargs):
        cls.calls += 1
        print("Meta.__call__ called")
        
        if cls.calls <= 2: #1 for singleton, any other number for multiton
            instance = object.__new__(cls)
            instance.__init__(*args, **kwargs)
            cls.data = instance  
            return instance
        else:
            instance = cls.data
            
            return instance


class Obj(metaclass=Meta):
    def __init__(self):
        print("Obj.__init__ called")

f = Obj()
g = Obj()
e = Obj()
pdb.set_trace()

a = 100

