#!/usr/bin/python3
MyClass = __import__('8-my_class').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

# Create an instance of MyClass
m = MyClass("John")
m.number = 89

# Print type and string representation of the object
print(type(m))
print(m)

# Convert object to JSON-serializable dictionary
mj = class_to_json(m)
print(type(mj))
print(mj)
