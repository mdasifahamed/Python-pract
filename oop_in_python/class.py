#Class is Like a Containter Which holds attributes, methods releted to its objects and its objects can use call attributes and methods by initiatiang an object of a class
#Like If Product is class then we can create object of product class like "Chocolate = Product()" Now this ChocoLate Object Can Access all Attributes methods of Product Class

#Creating a Class
class Student:
    pass# "Pass is Import bCause With out defining Attribute To a Class pass helps to bypass error no error has bess thrown "

#Initiating Student Class object
student1 = Student()

#Acccesing Attribute "However we Didin't Specify Any Attribute in the Class We can Also define attribute on the object for data types"
student1.name = "John"
student1.age = 27
student1.roll = 1056
student1.subject = "Economics"

print(type(student1))
print(student1.name)
print(student1.age)
print(student1.roll)
print(student1.subject)

