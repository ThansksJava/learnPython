# decorator
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# @log equals log = log(now)
@log
def now():
    print('2015-3-25')


now()


