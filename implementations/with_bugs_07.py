import json
from .store_order_processor_helpers import (
    types,
    brands,
    starting_value,
    StoreOrderProcessorException,
)


class ProcessorWithBugs07:  # explanation: still valid if exceeds inventory
    def __init__(self):
        self.inventory = {}

        # Initialize the inventory with the starting values.
        # for each type and brand combination in the store inventory, set the stock to be the starting value.
        for type in types:
            for brand in brands:
                self.set_current_inventory(type, brand, starting_value)

    def get_current_inventory(self, type, brand):
        """Returns the current inventory for a type and brand.
        We use a dictionary to store the values."""
        key = type + "_" + brand
        return self.inventory[key]

    def set_current_inventory(self, type, brand, value):
        """Sets the current inventory for a type and brand."""
        key = type + "_" + brand
        self.inventory[key] = value

    def process_list(self, list_of_items):
        """This method processes a list of order items."""
        for item in list_of_items:
            self.process_one_item(item)

        return self.get_result_string(list_of_items)

    def process_one_item(self, item):
        """This method processes a single item and updates the inventory accordingly."""
        type = item.get("type")
        brand = item.get("brand")
        quantity = item.get("quantity")

        if type not in types:
            raise StoreOrderProcessorException("Invalid item type")

        if brand not in brands:
            raise StoreOrderProcessorException("Invalid item brand")

        try:
            quantity = int(quantity)  # raises ValueError if not a number
        except ValueError:
            raise StoreOrderProcessorException("Invalid quantity")

        current_inventory = self.get_current_inventory(type, brand)
        current_inventory -= quantity

        self.set_current_inventory(type, brand, current_inventory)

    def get_result_string(self, list_of_items):
        """This method returns a string representation of the inventory.
        Types, brands, and quantities are separated by spaces.
        Each item is on a new line."""
        result = "Remaining inventory:\n"

        for type in types:
            for brand in brands:
                current_inventory = self.get_current_inventory(type, brand)
                result += f"{type} {brand} {current_inventory}\n"

        return result

    def process(self, filename):
        """This method processes a file containing a list of order items."""
        with open(filename, "r") as file:
            list_of_items = json.load(file)

        results = self.process_list(list_of_items)
        print(results)
