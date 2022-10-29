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

    def calculate_total_item_value(self):
        x = self.price * self.quantity
        print(f"Total Value For the product '{self.name}' is {x} USD For The Quantity '{self.quantity}' And Price Per Piece is '{self.price}' \n")
    def discounted_price(self):
        self.price = self.price -  (self.price * (self.discount/100)) #refers to line 3 and 35 and 37
        return f"New Discounted Price Will Be {self.price}"
    def __repr__(self):
        return f"Item('{self.name}','{self.price}','{self.quantity}')"#refers to line 40 - 44

#initiating a object of class Item
item1 = Item("Phone", 200,10)
item2 = Item("Airpod",100,50)
item3 = Item("Charger",50,100)
item4 = Item("Cable",20,200)
item5 = Item("Converter",10,250)
#without Changing Default Discount Rate
print(item1.discounted_price())
#After Setting New Discount Rate to the Item2
item2.discount = 30
print(item2.discounted_price())

#Displaying all the Objects Of The Class Which Has Been Created

print('\n')

print(Item.all)
