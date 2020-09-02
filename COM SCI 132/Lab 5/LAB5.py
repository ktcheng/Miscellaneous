# Lab 5

class SodaMachine:
    '''
        >>> m = SodaMachine('Coke', 10)
        >>> m.purchase()
        'Product out of stock'
        >>> m.restock(2)
        'Current soda stock: 2'
        >>> m.purchase()
        'Please deposit $10'
        >>> m.deposit(7)
        'Balance: $7'
        >>> m.purchase()
        'Please deposit $3'
        >>> m.deposit(5)
        'Balance: $12'
        >>> m.purchase()
        'Coke dispensed, take your $2'
        >>> m.deposit(10)
        'Balance: $10'
        >>> m.purchase()
        'Coke dispensed'
        >>> m.deposit(15)
        'Sorry, out of stock. Take your $15 back'
    '''
    
    def __init__(self, product, price):
    
        self.product = product
        self.price = price
        self.amount = 0
        self.balance = 0

    def purchase(self):
    
        if self.amount == 0:
            return "Product out of stock"
        
        elif self.balance < self.price:
            return ("Please deposit $" + str(self.price - self.balance))
        
        elif self.balance > self.price:
            self.amount -= 1 # Indicates valid purchase
            msg = (self.product.title() + " dispensed, take your $" + 
                    str(self.balance - self.price))
            self.balance = 0
            return msg
        
        elif self.balance == self.price:
            self.amount -= 1 # Indicates valid purchase
            self.balance = 0
            return (self.product.title() + " dispensed")

    def deposit(self, amount):
    
        if self.amount != 0:
            self.balance += amount
            return ("Balance: $" + str(self.balance))
        
        else:
            return ("Sorry, out of stock. Take your $" + str(amount) + 
                    " back")

    def restock(self, amount):
    
        self.amount += amount
        return ("Current soda stock: " + str(self.amount))
        
class Line:
    '''
        Creates objects of the class Line, takes 2 tuples. Class must have 2 PROPERTY methods
        >>> line1=Line((-7,-9),(1,5.6))
        >>> line1.distance
        16.648
        >>> line1.slope
        1.825
        >>> line2=Line((2,6),(2,3))
        >>> line2.distance
        3.0
        >>> line2.slope
        'Infinity'
    '''

    def __init__(self, coord1, coord2):
    
        self.coord1 = coord1
        self.coord2 = coord2

    @property
    def distance(self):
    
        x_coord1 = self.coord1[0]
        x_coord2 = self.coord2[0]
        y_coord1 = self.coord1[1]
        y_coord2 = self.coord2[1]
        
        x_value = (x_coord2 - x_coord1) ** 2
        y_value = (y_coord2 - y_coord1) ** 2
        
        distance = (x_value + y_value) ** 0.5
        distance = round(distance, 3)
        
        return distance
    
    @property
    def slope(self):
    
        y_rise = self.coord2[1] - self.coord1[1]
        x_rise = self.coord2[0] - self.coord1[0]
        
        try:
            slope = y_rise / x_rise
            slope = round(slope, 3)
            return slope
        except ZeroDivisionError:
            return ("Infinity")
