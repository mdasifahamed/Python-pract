#Class Can Have Constructure Which Can be used While initiating a Class  Object
# Creating Class that Will have Constructor Function
#Argunments that has pass can be by default if it not passed by the user while initiating objects like here roll argument and default arguments must be on the last parameter
#And Type of the argument can also specify by "argument_name : "data type like here name: str, birthdate: str ,subject: str and as we have se roll to by default 0 which mean its an integer so we don't need to specify that
class Student:
    def __init__(self, name: str, birthdate: str, subject: str, roll= 0):#This __init__ is Magic fucntion python Python has Many magic Function and the Self is Speacial keyword in pyhton Which refers the Object The of The class first while iniiating without it class will theow an error self can be changed with other word
        #Defining Attributes of the Class
        #here self.name refers to the object,name after initiating and the value will be the name which will be passed as parameter
        #refers to line 15 - 19
        self.name = name
        self.birthdate = birthdate
        self.roll = roll
        self.subject = subject
#Initiating a object
student1 = Student("Mark","1998-08-06","English",120)
print(student1.name)
print(student1.birthdate)
print(student1.subject)
print(student1.roll)

print('\n')
# Aonther Object Student Class With Default Argument
student2 = Student("Steve","1996-10-10","Math")# as here we did not specify the roll it will be by default 0 which is refrs to line 3 and 6
print(student2.name)
print(student2.birthdate)
print(student2.subject)
print(student2.roll)

