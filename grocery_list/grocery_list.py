# Accepts a series of inputted grocery items and writes them 
# to a .txt grocery list file in alphabetical order

def main():
    print('Grocery List Maker\n')
    groceries = []

    while True:
        item = input('Enter an item (<enter> to quit): ')
        if not item: break
        groceries.append(item)
    
    groceries.sort()
    grocery_file = open('grocery-list.txt', 'w')

    for item in groceries:
        print(item, file=grocery_file)

    grocery_file.close()
    print('\nList written to grocery-list.txt!')

main()