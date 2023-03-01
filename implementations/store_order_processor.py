import json
from .store_order_processor_helpers import (
    types,
    brands,
    starting_value,
    StoreOrderProcessorException,
)


class StoreOrderProcessor:
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
        """process a list of order items."""
        for item in list_of_items:
            self.process_one_item(item)

        return self.get_result_string(list_of_items)

    def process_one_item(self, item):
        """process a single item and update the inventory accordingly."""
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

        # it's ok if the inventory is 0, but if it is less than 0 the order was not valid.
        if current_inventory < 0:
            raise StoreOrderProcessorException("Out of stock")

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

        for brand in brands:
            if self.check_has_full_outfit_for_brand(list_of_items, brand):
                result += "This order contains a full outfit for a brand\n"
                break

        return result

    def check_has_full_outfit_for_brand(self, list_of_items, brand):
        """This method checks if an order has a full outfit for a given brand.
        A full outfit means we have the full set of jacket, slacks, and shoes for a given brand."""
        for type in types:
            if not self.search_in_list(list_of_items, type, brand):
                return False

        return True

    def search_in_list(self, list_of_items, type, brand):
        """Searches a list and returns True if matching item exists."""
        for item in list_of_items:
            if (
                item.get("type") == type
                and item.get("brand") == brand
                and int(item.get("quantity")) > 0
            ):
                return True

        return False

    def process(self, filename):
        """processes a file containing a list of order items."""
        with open(filename, "r") as file:
            list_of_items = json.load(file)

        results = self.process_list(list_of_items)
        print(results)
