# Docstrings practice with a GroceryItem class
"""Contains a GroceryItem class declaration"""

class GroceryItem:
    'A GroceryItem class'
    def __init__( self, id, name, price ):
        """
        Initializes a GroceryItem object with an id, name, and price
        example = GroceryItem(id, name, price)
        """
        self.id = id
        self.name = name
        self.price = price
        
    def priceForNItems( self, numOfItems ):
        'returns the price for n of a GroceryItem'
        return self.price * numOfItems
    
    def updateId( self, newId ):
        'updates the id variable of a GroceryItem'
        self.id = newId
        
    def getName( self ):
        'returns the name of a GroceryItem'
        return self.name

