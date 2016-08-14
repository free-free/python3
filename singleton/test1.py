# coding:utf-8
class S1(type):
    def __init__(cls, name, bases, dict):
        super(S1, cls).__init__(name, bases, dict)
        print("S.__init__(name=%s, bases=%s, dict=%s" %(name, bases, dict))
     
    def __call__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = super(S1, cls).__call__(*args, **kw)
        print("S.__call__(cls=%s, *args=%s, **kw=%s" %( cls, args, kw))
        return cls._instance



class MyClass1(object, metaclass=S1):
    pass


one = MyClass1()
two = MyClass1()

print(one)
print(two)
print(one == two)

