import functools
import time

'''
Custom decorators written to be used depending on the use cases
a) debug - Prints the function it is running and the outputs
b) do_twice - Runs a function twice
c) repaet(parameter) - Takes a parameter and repeats the function parameter times
'''

def debug(func):
    """Print the function signature and return value"""
    print("Running debug function")
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug


def do_twice(func):
    print("Running do_twice function")
    def do_twice_wrapper(*args,**kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)
    return do_twice_wrapper

''''
Decorator with arguments:The return value should be a decorator which takes in another function
                         Create a nested decorator,wrapper within the repeat block
'''
def repeat(num_times):
    print('Running repeat function')
    def decorator_repeat(func):
        def wrapper_decorator_repeat(*args,**kwargs):
            for i in range(num_times):
                value=func(*args,**kwargs)
            return value
        return wrapper_decorator_repeat
    return decorator_repeat


@repeat(10)
def greet(name):
    print(f'Hello,{name}')


greet("Vaishnavi")
