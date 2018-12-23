import types
# Function that prints the name of a passed in function, and returns a new function
# encapsulating the behavior of the original function
def notify(fn, *args, **kwargs):
    def fncomposite(*args, **kwargs):
        # Normal notify functionality
        print("running %s" % fn.__name__)
        rt = fn(*args, **kwargs)
        return rt
    # Return the composite function
    return fncomposite

# A metaclass that replaces methods of its classes
# with new methods 'enhanced' by the behavior of the composite function transformer
class Notifies(type):
    def __new__(cls, name, bases, attr):
        # Replace each function with
        # a print statement of the function name
        # followed by running the computation with the provided args and returning the computation result
        for name, value in attr.items():
            if type(value) is types.FunctionType or type(value) is types.MethodType:
                attr[name] = notify(value)
        return super(Notifies, cls).__new__(cls, name, bases, attr)

# Test the metaclass
class Math(metaclass=Notifies):
    def multiply(a, b):
        product = a * b
        print(product)
        return product

Math.multiply(5, 6)

# Running multiply():
# 30


class Shouter(metaclass=Notifies):
    def intro(self):
        print("I shout!")

s = Shouter()
s.intro()

# Running intro():
# I shout!
