# Minimum makefile impl github.com/Myriad-Dreamin/pymake
made = set()
def consume_makefile(method, *arg, **kwarg):
    if callable(method):
        i = str(method)
        if i not in made:
            made.add(i)
            method(*arg, **kwarg)

# return function in object scope
def sq(obj, attr):
    # raise if not exists
    def __get_object_attr(*_): return getattr(obj, attr)
    return __get_object_attr

# object requirements
def sqs(obj, *attrs): return map(lambda attr: sqs(obj, attr), attrs)

# return function in object scope
def oq(attr):
    # raise if not exists
    def __get_object_attr(obj, *_): return getattr(obj, attr)
    return __get_object_attr

# object requirements
def oqs(*attrs): return map(oq, attrs)

def require(*targets):
    def c(f):
        def wrapper(*args, **kwargs):
            for target in targets:
                target = (getattr(target, '__name__', None) == '__get_object_attr' and target(*args, **kwargs)) or target
                consume_makefile(target, *args, **kwargs)
            return f(*args, **kwargs)
        return wrapper
    return c
