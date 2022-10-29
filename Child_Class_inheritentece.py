import csv #A Module to work with csv file
#Student Class Will Be Our Parent Class
class Student:
    # An Class Attribute which can be Accesces the Class itself and also by the objects too see example at line 29 and 23
    student_type = "Regular"
    # An Class Attribute which can be Used To Store objects info And Can also be used to print all the  objects info by calling it after Class see the line 42
    all = []
    def __init__(self, name: str, b_date: str, sub: str, reg=0):
        # Validating Arguments
        assert reg >= 0, f"Roll Must Be Greater Than Zero Or Equal To Zero Not Negative {reg}"

        # Assingnign intansce attribute
        self.name = name
        self.b_date = b_date
        self.sub = sub
        self.reg = reg

        #Defining Class Attribute To Store all objects info
        Student.all.append(self)# As We are storing Of From tHe Class So the Class name Is Called and each object is appended to list becasue We Are Storing Objects Info


    # A Method Belongs To The Class
    def display_info(self):
        print("Name:  ", self.name)
        print("Birth_Date:  ", self.b_date)
        print("Subject:  ", self.sub)
        print("Reg No.:  ", self.reg)
        print("Student Type:  ", self.student_type)
    # An Magic Method display objects Info of The Class ProperLy Is repr

    #A Class Method To Instatiate Objects From Reading  CSV File
    @classmethod
    def initiate_obeject_from_csv(cls):
        with open("student.csv","r") as file:
            reader = csv.DictReader(file)
            students =list(reader)
            for items in students:
                Student(name = items.get("name"),
                     b_date = items.get("b_date"),
                     sub = items.get("sub"),
                     roll = int(items.get("reg")))

    def __repr__(self):
        return f"Student('{self.name}','{self.b_date}','{self.sub}','{self.reg}','{self.student_type}',{self.dept_roll})"






#Creating a New Class Named Management Which Will Inherit All The Attribute And Methods From The parent Student Class
class Manegement(Student):
    #Setting Constructor For This Class Which wIll be Same as Prent Class and New Attributes Can be Added Here
    def __init__(self,name: str, b_date: str, sub: str,reg=0,dept_roll=0):# Added new Attribute dept_roll
        #Validating Input
        assert dept_roll>=0, f"Department Roll Cannot Be Negative{dept_roll} It Must be greater or equal to 0"
        #Assinging Attribute To Thsi Class objects
        self.dept_roll = dept_roll
        '''
        Important this Super fucntions Helps to Bring All the Attributes And Method From the Parent class tro child class
        Here its Brings the Attribute and Methods FroM Student Class to Management class 
        '''
        super().__init__(
            name, b_date,sub,reg #In The built In init method Passing required attributes from the parent class
        )


#Creating Objects Of The Class Management And Passing Attributes field Of That Object
mangement1 = Manegement("Shahin","1996-03-16","Management",15681,10)
#Accesing Methods From the Parent Class See at 23 line
print(mangement1.display_info())
print('\n')
#Accesing Attributes From the Parent Class See from 7 and 43 line
print(mangement1.all)
#Overiding Parent Class Attribute Student_type from  line 5
mangement1.student_type ="Irregular"
print("\n")
print(mangement1.display_info())
