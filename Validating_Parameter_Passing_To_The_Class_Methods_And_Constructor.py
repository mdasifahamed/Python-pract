#By Using Assert keyword in the Methods We Can Validate Passed Parameter and Raise Error
# For Better Understnding Try to Run The Code First then Comment Out The Code From the Line 13-17 An Comment Out the code block From Line 20-24 Then Run The Programe again
class Student:
    def __init__(self, name: str,birthdate: str,subject: str, roll=0):
        #Validating Parmeter Input For Roll
        assert roll>=0, f"Roll Cannot be  Any Negative Number You Passed {roll}"
        #Setting Attributes
        self.name = name
        self.birthdate = birthdate
        self.subject = subject
        self.roll = roll

# Initiating An Object of Class Student
student1 = Student("Adam","2000-06-19","Bangla",-10)# as we have passed -10 it will rasie assertationerror refer to line 5-6
print(student1.name)
print(student1.birthdate)
print(student1.subject)
print(student1.roll)

# Initiating another  Object of Class Student
# student2 = Student("Adam","2000-06-19","Bangla",10)# This will Not Create any Error As Roll is Not an Negative Number Here
# print(student2.name)
# print(student2.birthdate)
# print(student2.subject)
# print(student2.roll)


