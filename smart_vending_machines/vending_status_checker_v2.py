# Processes vending machine data from JSON files and produces either a
# report on the status of the vending machines OR a sortable report 
# on beverages in the machines, including amount sold and current stock

from json import loads
from inventory_item import InventoryItem
from machine_status import MachineStatus

def process_file(file_name, inventory_dict, machine_dict):
    # Open and parse JSON file
    inventory_file = open(file_name, 'r')
    inventory_data = loads(inventory_file.read())
    inventory_file.close()

    # Initialize MachineStatus object for vending machine
    machine_label = inventory_data['machine_label']
    machine_status = MachineStatus(machine_label)
    machine_dict[machine_label] = machine_status
    sold_counts = {}

    # Loop through contents within inventory data and accumulate values to objects
    contents = inventory_data['contents']
    for row in contents:
        for slot in row['slots']:
            item_name = slot['item_name']
            inventory_item = inventory_dict.get(item_name, InventoryItem(item_name))

            last_stock = slot['last_stock']
            current_stock = slot['current_stock']
            price = slot['item_price']

            # Handle inventory item variables
            inventory_item.add_to_last_stock(last_stock)
            inventory_item.add_to_stock(current_stock)
            inventory_item.increment_slots()
            inventory_item.set_price(price)
            
            inventory_dict[item_name] = inventory_item

            # Handle machine status variables
            machine_status.add_previous_stock(last_stock)
            machine_status.add_in_stock(current_stock)

            # Keep a count of the total of each beverage sold
            current_count = sold_counts.get(item_name, 0)
            sold_counts[item_name] = current_count + (last_stock - current_stock)

    # Loop through sold counts and calculate income for file's machine
    for item in sold_counts:
        item_income = inventory_dict[item].get_total_price(sold_counts[item])
        machine_status.add_income(item_income)

def print_inventory(inventory_list):
    while True:
        # Get user prompt until valid input
        while True:
            sort_choice = input('Sort by (n) name, (p) pct sold, (s) stocking need, or (q) to quit: ')[0].lower()
            if sort_choice in ['n', 'p', 's', 'q']: break

        # Sort inventory list based on input or quit
        if sort_choice == 'q': 
            break
        elif sort_choice == 'n':
            inventory_list.sort(key=InventoryItem.get_name)
        elif sort_choice == 'p':
            inventory_list.sort(key=InventoryItem.get_sold_pct, reverse=True)
        elif sort_choice == 's':
            inventory_list.sort(key=InventoryItem.get_stock_need, reverse=True)
        
        # Print sorted inventory list
        print('\nItem Name            Sold     % Sold     In Stock Stock needs')
        for item in inventory_list:
            print('{:20} {:8} {:8.2f}% {:8} {:8}'.format(
                item.get_name(), item.get_number_sold(), item.get_sold_pct(), 
                item.get_in_stock(), item.get_stock_need()       
            ))
        print()

def print_machine_status(status_list):
    print('\nLabel           Pct Sold   Sales Total')
    for status in status_list:
        print('{:15} {:7.2f}%   ${:8.2f}'.format(
            status.get_label(), status.get_sold_pct(), status.get_income()
        )) 
    print()

def main():
    inventory_file_names = ['data/REID_1F_20171004.json', 'data/REID_2F_20171004.json', 'data/REID_3F_20171004.json']
    
    # Initialize object dictionaries
    item_inventory_dict = {}
    machine_status_dict = {}

    # Loop through each file and process its data
    for file_name in inventory_file_names:
        process_file(file_name, item_inventory_dict, machine_status_dict)

    item_inventory_list = list(item_inventory_dict.values())
    machine_status_list = list(machine_status_dict.values())

    # Handle printing user prompts and reports with sentinel looping
    while True:
        report_choice = input('Would you like the (m) machine report, the (i) inventory report, or (q) to quit? ')[0].lower()
        if report_choice == 'q':
            break
        elif report_choice == 'm':
            print_machine_status(machine_status_list)
        elif report_choice == 'i':
            print_inventory(item_inventory_list)
    
if __name__ == '__main__': main()