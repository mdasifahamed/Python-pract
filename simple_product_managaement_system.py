import csv
class Item:
    #Class Attributes
    discount = 20
    #Another Class Attributes For Storing Infos
    all = []# refres to Line 17
    #definig constructor
    def __init__(self,name: str, price=0, quantity= 0):
        #validating arguments
        assert price>=0 , f"price cannot be negative{price} it must be greater or equal to 0"
        assert quantity>=0 , f"quantity cannot be negative{quantity} it must be greater or equal to 0"
        #Setting Attributes For The Objects
        self.name = name
        self.price = price
        self.quantity = quantity

        #Adding Objects info of The Class To the List All
        Item.all.append(self)

    # A Class Method To Instatiate Objects From Reading  CSV File
    @classmethod
    def create_objects_from_csv(cls):
        with open("items.csv","r") as file:
            data = csv.DictReader(file)
            items = list(data)
            for item in items:# Iterarting Over The List which Gotten From The reader at Line
                #Important Here InItating objects of the Class Student Using The same as
                '''
                stu1 = Item("phone",10, 20)
                Just difference is  We are Passing the parameter From The Data We Have Gotten From the CSV 
                And Looping Through The All The row
                '''
                Item(name=item.get("name"),
                     price=float(item.get("price")),
                     quantity=int(item.get("quantity")))



    def calculate_total_item_value(self):
        x = self.price * self.quantity
        print(f"Total Value For the product '{self.name}' is {x} USD For The Quantity '{self.quantity}' And Price Per Piece is '{self.price}' \n")
    def discounted_price(self):
        self.price = self.price -  (self.price * (self.discount/100)) #refers to line 3 and 35 and 37
        return f"New Discounted Price Will Be {self.price}"
    def __repr__(self):
        return f"Item('{self.name}','{self.price}','{self.quantity}')"#refers to line 40 - 44

#initiating  object of class Item from a file
Item.create_objects_from_csv()
#Cheking The Items froM Class Attribute All Which Contash All the Object That Has Been
print(Item.all)
#We Can loop Through The List All And Access The Object Attribute Too For Example Se below
print("\n")
list_Of_items = Item.all
for i in list_Of_items:
    print(i.name)#Accesing object Attribute
    print(i.price)#Accesing object Attribute 
    print("\n")