# Special burger class

class SpecialBurger:
    def __init__( self, name, price ):
        self.name = name
        self.price = price

    def get_name( self ):
        return self.name

    def get_price( self ):
        return self.price
    
    def __repr__(self):
        return f'{self.get_name()} for ${self.get_price():0.2f}'

def main():
    burgers = [ SpecialBurger( 'Salvador Cauliflower Burger', 5.95), SpecialBurger( 'Chevre Which Way Burger', 6.95), SpecialBurger('Thank God it\'s Fried Egg Burger', 5.55)]

    burgers.append(SpecialBurger('Bob\'s Burger of the Day', 4.99))
    print(burgers)

    burgers.sort(key=SpecialBurger.get_name)
    print('\nSorted by name\n', burgers)

    burgers.sort(key=SpecialBurger.get_price)
    print('\nSorted by price\n', burgers)

if __name__ == '__main__': main()