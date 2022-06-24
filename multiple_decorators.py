'''
Decorators are used to change the functionality of a given function by wrapping them inside
a wrapper.When more than one decorator is called before a given function,the decorators are serviced from
bottom to top.
The first decorator takes the main function as the input function.
The second one takes the return value of the first decorator which is also a function as the input function
and so on.
It is therefor important to have a closure function within a decorator as the return type of the
wrapping function should be a function again so that the next decorator can pick it up and work on it

The below code shows the implementation of 3 decorators which can be used on the function "greet()"
'''

def uppercase(func):
    print("func_uppercase",func)
    def wrapper():
        original_function=func()
        print("original_function",original_function)
        new_function=original_function.upper()
        return new_function
    return wrapper
def split(func):
    print("func_split",func)
    def wrapper():
        #print("func",func)
        original=func()
        print("original",original)
        new_func=original.split()
        return new_func
    return wrapper
def lowercase(func):
    print("func_lowercase",func)
    def wrapper():
        original=func()
        new_func=[i.lower() for i in original]
        return new_func
    return wrapper

@lowercase
@split
@uppercase
def greet():
    return "hello there"

print(greet())

