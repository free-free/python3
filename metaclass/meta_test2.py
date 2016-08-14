# coding:utf-8


class Meta(type):
    
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print(" Meta.__prepare__(mcs=%s, name=%r, bases=%s, **%s" % (
            mcs, name, bases, kwargs))
        return {}
    
    def __new__(mcs, name, bases, attrs, **kwargs):
        print(" Meta.__new__(mcs=%s, name=%r, bases=%s, attrs=[%s], **%s" %(
            mcs, name, bases, ','.join(attrs), kwargs))
        return super().__new__(mcs, name, bases, attrs)
   
    def __init__(cls, name, bases, attrs, **kwargs):
        print(" Meta.__init__(cls=%s, name=%r, bases=%s, attrs=[%s], **%s" % (
            cls, name, bases, ','.join(attrs), kwargs))
        super().__init__(name, bases, attrs)
   
    def __call__(cls, *args, **kwargs):
        print(" Meta.__class__(cls=%s, args=%s, kwargs=%s" % (
            cls, args, kwargs))
        return super().__call__(*args, **kwargs)


class Class(metaclass=Meta, extra=1):
    def __new__(cls, myargs):
        print(' Class.__new__(cls=%s, myargs=%s' % (
            cls, myargs
        ))
        return super().__new__(cls)
      
    def __init__(self, myargs):
        print(" Class.__init__(self=%s, myargs=%s" %(
            self, myarsg
        ))
        self.myargs= myargs
        return super().__init__()

    def __str__(self):
        print("< instance of Class; myargs=%s>" %(
            getattr(self, 'myargs', "MISSING")
        ))
