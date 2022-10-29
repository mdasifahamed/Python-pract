#Class Attributes Are belongs class first and it Accesed by Objects Of The Class Too.
#CLass Attributes Can also be Overriden By Setting From the object See the Example FroM 23 and 33 to 34
class Student:
    #An Class Attribute whic can be Accesces the Class itself and also by the objects too see example at line 29 and 23
    student_type = "Regular"

    def __init__(self, name: str, b_date: str, sub: str, roll=0):

        #Validating Arguments
        assert roll>=0 ,f"Roll Must Be Greater Than Zero Or Equal To Zero Not Negative {roll}"

        #Assingnign intansce attribute
        self.name = name
        self.b_date = b_date
        self.sub = sub
        self.roll = roll
    #A Method Belongs To The Class
    def display_info(self):
        print("Name:  ",self.name)
        print("Birth_Date:  ",self.b_date)
        print("Subject:  ",self.sub)
        print("Roll:  ",self.roll)
        print("Student Type:  ", self.student_type)


#Creating Objects of Class Students
stu1 = Student("Kabir","1998-05-06","Accounting",150)

stu1.display_info()
print("\n")
print(stu1.student_type)
print("\n")
stu1.student_type = "Irregular"
stu1.display_info()