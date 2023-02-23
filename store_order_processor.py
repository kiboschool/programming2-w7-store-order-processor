import json


class InvalidOrderException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class StoreOrderProcessor:

    # The types and brands the store sells
    types = ['jacket', 'slacks', 'pair_of_shoes']
    brands = ['fruche', 'onalaja', 'kente']

    # The number of each item the store starts with
    starting_value = 20

    def __init__(self):
        self.inventory = {}
        # Initialize the inventory with the starting values
        # for each type and brand combination in the store inventory, set the stock to be the starting value
        for type in StoreOrderProcessor.types:
            for brand in StoreOrderProcessor.brands:
                key = (type, brand)
                self.inventory[key] = StoreOrderProcessor.starting_value

    """
    This method processes a list of order items."""

    def process_list(self, list_of_items):
        for item in list_of_items:
            self.process_one_item(item)

        return self.get_result_string()

    """
    This method processes a single item and updates the inventory accordingly."""

    def process_one_item(self, item):
        type = item.get('type')
        brand = item.get('brand')
        quantity = item.get('quantity')

        if item.get('type') not in StoreOrderProcessor.types:
            raise InvalidOrderException('Invalid item type')

        if item.get('brand') not in StoreOrderProcessor.brands:
            raise InvalidOrderException('Invalid item brand')

        quantity = int(quantity)  # raises ValueError if not a number

        key = (type, brand)

        if self.inventory[key] == 0:
            raise InvalidOrderException('Out of stock')

        if self.inventory[key] < quantity:

            raise InvalidOrderException('Not enough in stock')

        self.inventory[key] -= quantity

        return

    """
    This method returns a string representation of the inventory. 
    Types, brands, and quantities are separated by spaces. 
    Each item is on a new line."""

    def get_result_string(self):
        result = 'Remaining inventory:\n'

        for type in StoreOrderProcessor.types:
            for brand in StoreOrderProcessor.brands:
                key = (type, brand)
                result += f'{type} {brand} {self.inventory[key]}\n'

        return result

    """
    This method checks if the store has a full outfit for a given brand.
    A full outfit means we have the full set of jacket, slacks, and shoes for a given brand."""

    def check_has_full_outfit(self, brand):
        for type in StoreOrderProcessor.types:
            key = (type, brand)
            # if any of the items is less than the starting value, then we don't have a full outfit
            if self.inventory[key] < self.starting_value:
                return False

        return True

    """
    This method processes a file containing a list of order items."""

    def process(self, filename):
        with open(filename, 'r') as file:
            try:
                list_of_items = json.load(file)
            except:
                # self.is_valid = False
                list_of_items = []

        results = self.process_list(list_of_items)
        print(results)
