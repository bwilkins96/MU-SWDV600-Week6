# Shopping cart class

from grocery_item import GroceryItem

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def addItem(self, item):
        self.items.append(item)
    
    def getCartTotal(self):
        total = 0.0
        for item in self.items:
            total += item.priceForNItems(1)
        
        return total

def main():
    example = GroceryItem(1, 'lemonade', 2.99)
    example2 = GroceryItem(2, 'cheese', 4.99)

    cartExample = ShoppingCart()
    cartExample.addItem(example)
    cartExample.addItem(example2)

    print(cartExample.getCartTotal())

if __name__ == '__main__': main()

