#Varibales in Python
'''
Python is dynamic language it does need data type declaration
every python variable is a object and it refers to the class of its data type
python program reads line by line.
Note : str with int or  float  cannot be concatenated it will need type casting.
'''


#
a = 10
print(a)

b = 20

print(a+b)

b = 30
# b  + b will generate 60 because b has been updated to 30 on the next assigning so it will not generate 50 as code is gointo inetrpreted by line by line

print(b+b)

# python does not require data type as it is dynamic language example below
# x will be int type and y will float

x = 5
y = 7.5
print(x+y)

# we can also assign string value to the variable

k = "Hello, how are you"
print(k)

# string concatenation
j = "Asif"

i = "?"
print(k+" " +j + i)

#  Empty string
l = ""
print(l)


