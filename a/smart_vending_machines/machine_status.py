# Machine status class

# the label of a vending machine

# the total amount of beverages the vending machine was previously stocked with

# the total amount of beverages currently in stock in the vending machine

# the total income of the machine from the last time it was stocked until now 
# (note: beverages have different prices, so you cannot simply multiply 
# the change in stock times $1.50 to get the total income)

class MachineStatus:
    def __init__(self, label):
        self.label = label
        self.total_previous_stock = 0
        self.total_in_stock = 0
        self.total_income = 0.0
    
    def get_label(self):
        return self.label
    
    def get_previous_stock(self):
        return self.total_previous_stock
    
    def get_in_stock(self):
        return self.total_in_stock
    
    def get_income(self):
        return self.total_income
    
    def add_previous_stock(self, amt):
        self.total_previous_stock += amt
    
    def add_in_stock(self, amt):
        self.total_in_stock += amt

    def add_income(self, amt):
        self.total_income += amt 
    
    def get_sold(self):
        return self.get_previous_stock() - self.get_in_stock()
    
    def get_sold_pct(self):
        return (self.get_sold() / self.get_previous_stock()) * 100

    def __repr__(self):
        return '{' + f'Label: {self.get_label()}, Previous Stock: {self.get_previous_stock()}, Current Stock: {self.get_in_stock()}, Income: {self.get_income()}' + '}'