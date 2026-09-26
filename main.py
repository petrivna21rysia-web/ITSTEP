name = [5,6]
print(type(name))

name = "hello"
print(dir(name))
print(name.upper())

name = "Python"
print(hasattr(name, "fly"))

test ="hello"
method = getattr(text, "upper")
print(method)

import inspect
def hello():
   print("Hello World")
class Cat:
  pass
print (inspect.isfunction(hello))
print (inspect.isclass(Cat))

import sys
print(sys.version)
print(sys.platform)