import csv #A Module to work with csv file
#As We Know A Method is Known As Fucmtion of Classand By default  it takes deafult Argument as object which is called self inside class while definning fucntion
#But A Class Method is A Special Type of Method Which Takes Default Argument as The Class it self And Before Assinging The Class We Need To Specif Decorator Like @classmethod
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

    #A Class Method To Instatiate Objects From Reading  CSV File
    @classmethod
    def initiate_obeject_from_csv(cls):#Notice Here Inside The Functions Argument cls is automatic came with Definantion of @classmethod before the functions defining That is Default and withot can not be used
        with open("student.csv","r") as file: #Usual Statment For Working With File
            reader = csv.DictReader(file) #Reading CSV File Through Csv module and Converting its value toA Distionary and Storing To Reader Variable
            students =list(reader)# Converting The reader data To A List
            for items in students:# Iterarting Over The List which Gotten From The reader at Line 36
                #Important Here InItating objects of the Class Student Using The same as
                '''
                stu1 = Student("Arif","1996-12-19", "Management", 10)
                Just difference is  We are Passing the parameter From The Data We Have Gotten From the CSV 
                And Looping Throgh The All The row
                '''
                Student(name = items.get("name"),
                     b_date = items.get("b_date"),
                     sub = items.get("sub"),
                     roll = int(items.get("roll")))

    def __repr__(self):#Again Its Self By Default For As it refers to the objects
        return f"Student('{self.name}','{self.b_date}','{self.sub}','{self.roll}','{self.student_type}')"


# Creating Objects of Class Students

Student.initiate_obeject_from_csv()#Calling The Class Method From The Class  created object From A Csv File .Note We Can also Call this Method From a Object see at line57
# stu1 = Student("AAA","BBB","CCC")
# print(stu1.initiate_obeject_from_csv())
list_of_students = Student.all # Storing The Collections Of The oobjects froM Class Attribute Which is a List
#Looping Through The list_of_students
for i in list_of_students:
    print(i)
print("\n")
#We Can Also Access The Attribute Of The Objects That Has Been Created From The Csv See Example Below
for i in list_of_students:
    print(i.name)