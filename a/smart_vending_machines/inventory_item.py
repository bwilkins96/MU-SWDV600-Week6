# Inventory item class

class InventoryItem:
    def __init__(self, name):
        self.name = name
        self.last_stocked = 0
        self.total_in_stock = 0
        self.total_slots = 0
        self.price = 0
    
    def get_name(self):
        return self.name

    def get_last_stock(self):
        return self.last_stocked
    
    def get_in_stock(self):
        return self.total_in_stock
    
    def get_slots(self):
        return self.total_slots

    def get_price(self):
        return self.price

    def add_to_last_stock(self, amt):
        self.last_stocked += amt

    def add_to_stock(self, amt):
        self.total_in_stock += amt
    
    def increment_slots(self):
        self.total_slots += 1
    
    def set_price(self, price):
        self.price = price
    
    def get_total_price(self, n):
        return self.get_price() * n
    
    def get_number_sold(self):
        return self.get_last_stock() - self.get_in_stock()
    
    def get_income(self):
        return self.get_number_sold() * self.get_price()
    
    def get_sold_pct(self):
        return (self.get_number_sold() / self.get_last_stock()) * 100
    
    def get_stock_need(self):
        return (8 * self.get_slots()) - self.get_in_stock()
    
    def __repr__(self):
        return '{' + f'Name: {self.get_name()}, In Stock: {self.get_in_stock()}, Last Stocked: {self.get_last_stock()}, Slots: {self.get_slots()}, Price: {self.get_price()}' + '}'