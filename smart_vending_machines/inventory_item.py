# Inventory item class

class InventoryItem:
    'An inventory item class designed for Maryville University'
    def __init__(self, name):
        """
        Initializes an InventoryItem object with name, last stocked,
        current stock, total slots, and price variables
        e.g. InventoryItem(name)
        """
        self.name = name
        self.last_stocked = 0
        self.total_in_stock = 0
        self.total_slots = 0
        self.price = 0
    
    def get_name(self):
        'Returns the name variable'
        return self.name

    def get_last_stock(self):
        'Returns the last stocked variable'
        return self.last_stocked
    
    def get_in_stock(self):
        'Returns the current stock variable'
        return self.total_in_stock
    
    def get_slots(self):
        'Returns the total slots variable'
        return self.total_slots

    def get_price(self):
        'Returns the price variable'
        return self.price

    def add_to_last_stock(self, amt):
        'Adds amt to the last stocked variable'
        self.last_stocked += amt

    def add_to_stock(self, amt):
        'Adds amt to the current stock variable'
        self.total_in_stock += amt
    
    def increment_slots(self):
        'Increments the total slots variable by 1'
        self.total_slots += 1
    
    def set_price(self, price):
        'Sets the price variable'
        self.price = price
    
    def get_total_price(self, n):
        'Calculates and returns the price n number of the item'
        return self.get_price() * n
    
    def get_number_sold(self):
        'Calculates and returns the total number sold'
        return self.get_last_stock() - self.get_in_stock()
    
    def get_income(self):
        'Calculates and returns the total income since last stock'
        return self.get_number_sold() * self.get_price()
    
    def get_sold_pct(self):
        'Calculates and returns the percentage sold'
        return (self.get_number_sold() / self.get_last_stock()) * 100
    
    def get_stock_need(self):
        'Calculates and returns the stock need'
        return (8 * self.get_slots()) - self.get_in_stock()
    
    def __repr__(self):
        return '{' + f'Name: {self.get_name()}, In Stock: {self.get_in_stock()}, Last Stocked: {self.get_last_stock()}, Slots: {self.get_slots()}, Price: {self.get_price()}' + '}'