#Methods Are SameFunctions When Declare A Fiucntion Inside A Class Then We It Method of That Class And we can Call that Method to the Objects of that Class
class Student:
    def __init__(self, name : str, birthdate: str, subject: str, roll = 0):
       #Validating Argument
        assert roll>=0, f"The Roll  Cannot Be a Negative Number{roll} "
        #Setting Attributes
        self.name = name
        self.birthdate = birthdate
        self.subject = subject
        self.roll = roll
    #Creating A Simple Methods
    #Which will display objects Info that Has Been Passed To The Constructor refers to the line 3
    #Important! Here again self refers to The Object of The classs that will be Created later after initiating class object here from line 21 evertime any object this class will have access to that fucntion
    def display_info(self):
        print("Student Name : ",self.name)
        print("Birthdate : ",self.birthdate)
        print("Subject : ",self.subject)
        print("Roll : ",self.roll)

#Inintiating a object of Class Student
student_1 = Student("karim","1996-06-10","History",150)
#Calling The Fucntion On the object
student_1.display_info()

print('\n')
#Another Example
student_2 =Student("Rahim","2005-29-10","Geography",250)
student_2.display_info()