# getting User input Using input() finction
"""note input() functions return only string whether it is number or character it will be string
To do mathematical operation after input type conversion is needed"""

#Without type conversion it will string concatenation
print("Enter a value: ")

a  = input()
print("Enter another value: ")
b  = input()

print("without Type conversion "+a+b)

#With type conversion
print("with type conversion to int "+str(int(a) + int(b))) # as print has both str and int type str and int can not be joined so str conversion whole summation is needed

#Display message inside input ()

x = input("enter an number : ")
y = input("enter another Number : ")
z = int(x) * int(y)

print("Multipication of Two number Is :  "+str(z))





