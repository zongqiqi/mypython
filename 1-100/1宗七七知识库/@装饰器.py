"""装饰器"""

#代码运行期间动态增加功能
#不带参数=====================================================
def log(func):
    def warpper(*args,**kw):
        print ('call %s():'%func.__name__)
        return func(*args,**kw)
    return warpper
@log
def now():
    print("2013-12-25")
now()
#带参数========================================================
def log(text):
    def decorator(func):
        def warpper(*args,**kw):
            print("%s %s():"%(text,func.__name__))
            return func(*args,**kw))
        return warpper
    return decorator
@log('execute')
def now():
    return ('2013-12-25')
now()
