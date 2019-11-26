import functools


def log(text):
    def decorator(func):
        # keep original function signature
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# equal now = log('execute')(now)
@log('execute')
def now():
    print('2015-3-25')


now()

print(now.__name__)