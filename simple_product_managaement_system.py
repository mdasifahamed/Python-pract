class Item:
    #definig constructor
    def __init__(self,name: str, price=0, quantity= 0):
        #validating arguments
        assert price>=0 , f"price cannot be negative{price} it must be greater or equal to 0"
        assert quantity>=0 , f"quantity cannot be negative{quantity} it must be greater or equal to 0"
        #Setting Attributes
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_item_value(self):
        x = self.price * self.quantity
        print(f"Total Value For the product '{self.name}' is {x} USD For The Quantity '{self.quantity}' And Price Per Piece is '{self.price}' \n")
#initiating a object of class Item
item1 = Item("Phone", 170,10)
item2 = Item("Airpod",50,50)
item1.calculate_total_item_value()
item2.calculate_total_item_value()
