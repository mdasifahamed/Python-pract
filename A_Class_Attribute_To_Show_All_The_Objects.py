# Class Attributes Are belongs class first and it Accesed by Objects Of The Class Too.
# CLass Attributes Can also be Overriden By Setting From the object See the Example FroM 23 and 33 to 34
class Student:
    # An Class Attribute which can be Accesces the Class itself and also by the objects too see example at line 29 and 23
    student_type = "Regular"
    # An Class Attribute which can be Used To Store objects info And Can also be used to print all the  objects info by calling it after Class see the line 42
    all = []
    def __init__(self, name: str, b_date: str, sub: str, roll=0):
        # Validating Arguments
        assert roll >= 0, f"Roll Must Be Greater Than Zero Or Equal To Zero Not Negative {roll}"

        # Assingnign intansce attribute
        self.name = name
        self.b_date = b_date
        self.sub = sub
        self.roll = roll

        #Defining Class Attribute To Store all objects info
        Student.all.append(self)# As We are storing Of From tHe Class So the Class name Is Called and each object is appended to list becasue We Are Storing Objects Info


    # A Method Belongs To The Class
    def display_info(self):
        print("Name:  ", self.name)
        print("Birth_Date:  ", self.b_date)
        print("Subject:  ", self.sub)
        print("Roll:  ", self.roll)
        print("Student Type:  ", self.student_type)
    # An Magic Method display objects Info of The Class ProperLy Is repr

    def __repr__(self):#Again Its Self By Default For As it refers to the objects
        return f"Student('{self.name}','{self.b_date}','{self.sub}','{self.roll}','{self.student_type}')"


# Creating Objects of Class Students
stu1 = Student("Kabir", "1998-05-06", "Accounting", 150)
stu2 = Student("Karim", "1995-04-25", "Marketing", 550)
stu3 = Student("Kamal", "1997-10-15", "Management", 355)
stu4 = Student("Khan", "1999-07-16", "Finance", 450)
stu5 = Student("Kamrul", "1996-11-20", "HRM", 250)

print(Student.all)