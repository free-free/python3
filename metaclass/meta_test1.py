# coding:utf-8

class DBInterfaceMeta(type):
    
    def __init__(cls, name, base, attrs):
        if not hasattr(cls, 'registry'):
            print("create registry==>",cls)
            print(name)
            print(base)
            print(attrs)
            cls.registry = {}
        else:
            interface_id = name.lower()
            cls.registry[interface_id] = cls
        super(DBInterfaceMeta, cls).__init__(name, base, attrs)
   

class DBInterface(object, metaclass=DBInterfaceMeta):
    pass


print(DBInterface.registry)


class FirstInterface(DBInterface):
    pass


class SecondInteface(DBInterface):
    pass


class ThirdInterface(DBInterface):
    pass


print(DBInterface.registry)
