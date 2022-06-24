'''
@classmethod decorator is used for giving default values when the input has different datatypes.
Since a given class can only have one constructor, the decorator can be used for setting default values to
the inputs

'''

class Datatypes:
    def __init__(self,*args):
        print(args)
        self.args=list(args[0])

    def __call__(self):
        return(self.args)

    @classmethod
    def from_list(cls,arglist):

        arg=tuple(arglist)
        instance=cls(arg)
        return instance
    @classmethod
    def from_tuple(cls,arglist):

        instance=cls(arglist)
        return instance
    @classmethod
    def from_dict(cls,arglist):
        values=arglist.values()
        instance=cls(tuple(values))
        return instance

list1=Datatypes.from_list(["one","two","three","four"])
tuple1=Datatypes.from_tuple(("one","two","three"))
dict1=Datatypes.from_dict({1:"one",2:"two",3:"three"})

print(list1())
print(tuple1())
print(dict1())

