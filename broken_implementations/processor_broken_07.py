
import json
from ..store_order_processor_helpers import types, brands, starting_value, StoreOrderProcessorException

class ProcessorBroken07: # explanation: still valid if exceeds inventory
    def __init__(self):
        self.inventory = {}
        
        # Initialize the inventory with the starting values.
        # for each type and brand combination in the store inventory, set the stock to be the starting value.
        for type in types:
            for brand in brands:
                self.set_current_inventory(type, brand, starting_value)

    """Returns the current inventory for a type and brand.
    We use a dictionary to store the values."""
    def get_current_inventory(self, type, brand):
        key = type + '_' + brand
        return self.inventory[key]
        
    """Sets the current inventory for a type and brand."""
    def set_current_inventory(self, type, brand, value):
        key = type + '_' + brand
        self.inventory[key] = value

    """This method processes a list of order items."""
    def process_list(self, list_of_items):
        for item in list_of_items:
            self.process_one_item(item)

        return self.get_result_string(list_of_items)

    """This method processes a single item and updates the inventory accordingly."""
    def process_one_item(self, item):
        type = item.get('type')
        brand = item.get('brand')
        quantity = item.get('quantity')

        if type not in types:
            raise StoreOrderProcessorException('Invalid item type')
            
        if brand not in brands:
            raise StoreOrderProcessorException('Invalid item brand')

        try:
            quantity = int(quantity)  # raises ValueError if not a number
        except ValueError:
            raise StoreOrderProcessorException('Invalid quantity')
        
        current_inventory = self.get_current_inventory(type, brand)
        current_inventory -= quantity
        
        
        self.set_current_inventory(type, brand, current_inventory)

    """This method returns a string representation of the inventory. 
    Types, brands, and quantities are separated by spaces. 
    Each item is on a new line."""
    def get_result_string(self, list_of_items):
        result = 'Remaining inventory:\n'

        for type in types:
            for brand in brands:
                current_inventory = self.get_current_inventory(type, brand)
                result += f'{type} {brand} {current_inventory}\n'
                
        for brand in brands:
            if self.check_has_full_outfit_for_brand(list_of_items, brand):
                result += 'Contains full outfit for a brand\n'
                break

        return result

    
    """This method checks if an order has a full outfit for a given brand.
    A full outfit means we have the full set of jacket, slacks, and shoes for a given brand."""
    def check_has_full_outfit_for_brand(self, list_of_items, brand):
        for type in types:
            if not self.search_in_list(list_of_items, type, brand):
                return False

        return True
        
    
    """Searches a list and returns True if exists."""
    def search_in_list(self, list_of_items, type, brand):
        for item in list_of_items:
            if item.get('type') == type and item.get('brand') == brand and int(item.get('quantity')) > 0:
                return True
        
        return False

    """This method processes a file containing a list of order items."""
    def process(self, filename):
        with open(filename, 'r') as file:
            list_of_items = json.load(file)
        
        results = self.process_list(list_of_items)
        print(results)


