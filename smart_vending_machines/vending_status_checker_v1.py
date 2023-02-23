# Processes vending machine data from JSON files and produces a sortable report 
# on beverages in the machines, including amount sold and current stock

from json import loads
from inventory_item import InventoryItem

def main():
    inventory_file_names = ['data/REID_1F_20171004.json', 'data/REID_2F_20171004.json', 'data/REID_3F_20171004.json']
    
    item_inventory_dict = {}
    for file_name in inventory_file_names:
        inventory_file = open(file_name, 'r')
        inventory_data = loads(inventory_file.read())
        inventory_file.close()

        contents = inventory_data['contents']

        for row in contents:
            for slot in row['slots']:
                item_name = slot['item_name']

                inventory_item = item_inventory_dict.get(item_name, InventoryItem(item_name))
                
                inventory_item.add_to_last_stock(slot['last_stock'])
                inventory_item.add_to_stock(slot['current_stock'])
                inventory_item.increment_slots()
                
                item_inventory_dict[item_name] = inventory_item

    item_inventory_list = list(item_inventory_dict.values())

    while True:
        sort_choice = input('Sort by (n) name, (p) pct sold, (s) stocking need, or (q) to quit: ')[0].lower()

        if sort_choice == 'q': 
            break
        elif sort_choice == 'n':
            item_inventory_list.sort(key=InventoryItem.get_name)
        elif sort_choice == 'p':
            item_inventory_list.sort(key=InventoryItem.get_sold_pct, reverse=True)
        elif sort_choice == 's':
            item_inventory_list.sort(key=InventoryItem.get_stock_need, reverse=True)
        
        print('Item Name            Sold     % Sold     In Stock Stock needs')
        for item in item_inventory_list:
            print('{:20} {:8} {:8.2f}% {:8} {:8}'.format(
                item.get_name(), item.get_number_sold(), item.get_sold_pct(), 
                item.get_in_stock(), item.get_stock_need()       
            ))
        print()

main()