# Machine status class

class MachineStatus:
    'A machine status class designed for Maryville University'
    def __init__(self, label):
        """
        Initializes a MachineStatus object with label, total previous stock, 
        total current stock, and total income variables
        e.g. MachineStatus(label) 
        """
        self.label = label
        self.total_previous_stock = 0
        self.total_in_stock = 0
        self.total_income = 0.0
    
    def get_label(self):
        'Returns the label variable'
        return self.label
    
    def get_previous_stock(self):
        'Returns the total previous stock variable'
        return self.total_previous_stock
    
    def get_in_stock(self):
        'Returns the total current stock variable'
        return self.total_in_stock
    
    def get_income(self):
        'Returns the total income since last stock variable'
        return self.total_income
    
    def add_previous_stock(self, amt):
        'Adds amt to the total previous stock variable'
        self.total_previous_stock += amt
    
    def add_in_stock(self, amt):
        'Adds amt to total current stock variable'
        self.total_in_stock += amt

    def add_income(self, amt):
        'Adds amt to total income variable'
        self.total_income += amt 
    
    def get_sold(self):
        'Calculates and returns the total number of items sold'
        return self.get_previous_stock() - self.get_in_stock()
    
    def get_sold_pct(self):
        'Calculates and returns the percentage of items sold'
        return (self.get_sold() / self.get_previous_stock()) * 100

    def __repr__(self):
        return '{' + f'Label: {self.get_label()}, Previous Stock: {self.get_previous_stock()}, Current Stock: {self.get_in_stock()}, Income: {self.get_income()}' + '}'