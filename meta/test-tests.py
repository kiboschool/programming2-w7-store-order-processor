
import sys
sys.path.append('..')
import test_store_order_processor
from main import starting_value, types, brands
starting_value = 20

# provide a bunch of broken implementations:
# the tests running with these implementations should fail.

# the 'explanation' comments won't be in the copy of this file given to students

# this is a long file so students can't cheat by copying a working file in from here.
# (but no need to make it truly hidden)
# it's ok that a student could complete the first part of the assignment by copying a class here
# and fixing it, if they do that more power to them :p
# could put a working class and inherit, but then students could see this

class ExampleImpl001:
    def __init__(self):
        self.inventory = {}
        for type in types:
            for brand in brands:
                key = (type, brand)
                self.inventory[key] = starting_value

        self.is_valid = True

    def process_list(self, list_of_items):
        for item in list_of_items:
            self.process_one_item(item)

        self.check_has_full_outfit()
        return self.get_result_string()

    def process(self, filename):
        with open(filename, 'r') as file:
            try:
                list_of_items = json.load(file)
            except:
                self.is_valid = False
                list_of_items = []

        results = self.process_list(list_of_items)
        print(results)

    def process_one_item(self, item):
        type = item['type']
        brand = item.get('brand')
        quantity = item.get('quantity')

        if item.get('brand') not in brands:
            self.is_valid = False
            return

        try:
            quantity = int(quantity)
        except ValueError:
            self.is_valid = False
            return

        key = (type, brand)
        if key not in self.inventory:
            self.inventory[key] = starting_value
        self.inventory[key] -= quantity
        if self.inventory[key] < 0:
            self.is_valid = False
            return

    def check_has_full_outfit(self):
        self.has_full_outfit = False
        for brand in brands:
            is_full_for_this_brand_so_far = True
            for type in types:
                key = (type, brand)
                if self.inventory[key] == starting_value:
                    is_full_for_this_brand_so_far = False

            if is_full_for_this_brand_so_far:
                self.has_full_outfit = True

    def get_result_string(self):
        if not self.is_valid:
            return 'Invalid input'

        results = 'Remaining inventory:\n'
        for type in types:
            for brand in brands:
                key = (type, brand)
                results += f'{type} {brand} {self.inventory[key]}\n'

        if self.has_full_outfit:
            results += 'Contains full outfit for a brand\n'

        return results


class ExampleImpl002:
    def __init__(self):
        self.inventory = {}
        for type in types:
            for brand in brands:
                key = (type, brand)
                self.inventory[key] = starting_value

        self.is_valid = True

    def process_list(self, list_of_items):
        for item in list_of_items:
            self.process_one_item(item)

        self.check_has_full_outfit()
        return self.get_result_string()

    def process(self, filename):
        with open(filename, 'r') as file:
            try:
                list_of_items = json.load(file)
            except:
                self.is_valid = False
                list_of_items = []

        results = self.process_list(list_of_items)
        print(results)

    def process_one_item(self, item):
        type = item.get('type')
        brand = item['brand']
        quantity = item.get('quantity')

        if item.get('type') not in types:
            self.is_valid = False
            return

        try:
            quantity = int(quantity)
        except ValueError:
            self.is_valid = False
            return

        key = (type, brand)
        if key not in self.inventory:
            self.inventory[key] = starting_value
        self.inventory[key] -= quantity
        if self.inventory[key] < 0:
            self.is_valid = False
            return

    def check_has_full_outfit(self):
        self.has_full_outfit = False
        for brand in brands:
            is_full_for_this_brand_so_far = True
            for type in types:
                key = (type, brand)
                if self.inventory[key] == starting_value:
                    is_full_for_this_brand_so_far = False

            if is_full_for_this_brand_so_far:
                self.has_full_outfit = True

    def get_result_string(self):
        if not self.is_valid:
            return 'Invalid input'

        results = 'Remaining inventory:\n'
        for type in types:
            for brand in brands:
                key = (type, brand)
                results += f'{type} {brand} {self.inventory[key]}\n'

        if self.has_full_outfit:
            results += 'Contains full outfit for a brand\n'

        return results

class ExampleImpl003:
    def __init__(self):
        self.inventory = {}
        for type in types:
            for brand in brands:
                key = (type, brand)
                self.inventory[key] = starting_value

        self.is_valid = True

    def process_list(self, list_of_items):
        for item in list_of_items:
            self.process_one_item(item)

        self.check_has_full_outfit()
        return self.get_result_string()

    def process(self, filename):
        with open(filename, 'r') as file:
            try:
                list_of_items = json.load(file)
            except:
                self.is_valid = False
                list_of_items = []

        results = self.process_list(list_of_items)
        print(results)

    def process_one_item(self, item):
        type = item.get('type')
        brand = item.get('brand')
        quantity = item.get('quantity')

        if item.get('type') not in types:
            self.is_valid = False
            return

        if item.get('brand') not in brands:
            self.is_valid = False
            return

        if not quantity and not str(quantity).strip() == '0':
            raise ValueError()
        else:
            try:
                quantity = int(quantity)
            except ValueError:
                self.is_valid = False
                return

        key = (type, brand)
        if key not in self.inventory:
            self.inventory[key] = starting_value
        self.inventory[key] -= quantity
        if self.inventory[key] < 0:
            self.is_valid = False
            return

    def check_has_full_outfit(self):
        self.has_full_outfit = False
        for brand in brands:
            is_full_for_this_brand_so_far = True
            for type in types:
                key = (type, brand)
                if self.inventory[key] == starting_value:
                    is_full_for_this_brand_so_far = False

            if is_full_for_this_brand_so_far:
                self.has_full_outfit = True

    def get_result_string(self):
        if not self.is_valid:
            return 'Invalid input'

        results = 'Remaining inventory:\n'
        for type in types:
            for brand in brands:
                key = (type, brand)
                results += f'{type} {brand} {self.inventory[key]}\n'

        if self.has_full_outfit:
            results += 'Contains full outfit for a brand\n'

        return results

class ExampleImpl004:
    def __init__(self):
        self.inventory = {}
        for type in types:
            for brand in brands:
                key = (type, brand)
                self.inventory[key] = starting_value

        self.is_valid = True

    def process_list(self, list_of_items):
        for item in list_of_items:
            self.process_one_item(item)

        self.check_has_full_outfit()
        return self.get_result_string()

    def process(self, filename):
        with open(filename, 'r') as file:
            try:
                list_of_items = json.load(file)
            except:
                self.is_valid = False
                list_of_items = []

        results = self.process_list(list_of_items)
        print(results)

    def process_one_item(self, item):
        type = item.get('type')
        brand = item.get('brand')
        quantity = item.get('quantity')

        if item.get('type') not in types:
            self.is_valid = False
            return

        if item.get('brand') not in brands:
            self.is_valid = False
            return

        if not quantity and not str(quantity).strip() == '0':
            try:
                quantity = int(quantity)
            except ValueError:
                self.is_valid = False
                return
        else:
            quantity = int(quantity)

        key = (type, brand)
        self.inventory[key] -= quantity
        if self.inventory[key] < 0:
            self.is_valid = False
            return

    def check_has_full_outfit(self):
        self.has_full_outfit = False
        for brand in brands:
            is_full_for_this_brand_so_far = True
            for type in types:
                key = (type, brand)
                if self.inventory[key] == starting_value:
                    is_full_for_this_brand_so_far = False

            if is_full_for_this_brand_so_far:
                self.has_full_outfit = True

    def get_result_string(self):
        if not self.is_valid:
            return 'Invalid input'

        results = 'Remaining inventory:\n'
        for type in types:
            for brand in brands:
                key = (type, brand)
                results += f'{type} {brand} {self.inventory[key]}\n'

        if self.has_full_outfit:
            results += 'Contains full outfit for a brand\n'

        return results

class ExampleImpl005:
    def __init__(self):
        self.inventory = {}
        for type in types:
            for brand in brands:
                key = (type, brand)
                self.inventory[key] = starting_value

        self.is_valid = True

    def process_list(self, list_of_items):
        for item in list_of_items:
            self.process_one_item(item)

        self.check_has_full_outfit()
        return self.get_result_string()

    def process(self, filename):
        with open(filename, 'r') as file:
            try:
                list_of_items = json.load(file)
            except:
                self.is_valid = False
                list_of_items = []

        results = self.process_list(list_of_items)
        print(results)

    def process_one_item(self, item):
        type = item.get('type')
        brand = item.get('brand')
        quantity = item.get('quantity')

        if item.get('type') not in types:
            self.is_valid = False
            return

        if item.get('brand') not in brands:
            self.is_valid = False
            return

        try:
            quantity = int(quantity)
        except ValueError:
            self.is_valid = False
            return

        key = (type, brand)
        self.inventory[key] -= quantity
        if quantity > starting_value:
            self.is_valid = False
            return

    def check_has_full_outfit(self):
        self.has_full_outfit = False
        for brand in brands:
            is_full_for_this_brand_so_far = True
            for type in types:
                key = (type, brand)
                if self.inventory[key] == starting_value:
                    is_full_for_this_brand_so_far = False

            if is_full_for_this_brand_so_far:
                self.has_full_outfit = True

    def get_result_string(self):
        if not self.is_valid:
            return 'Invalid input'

        results = 'Remaining inventory:\n'
        for type in types:
            for brand in brands:
                key = (type, brand)
                results += f'{type} {brand} {self.inventory[key]}\n'

        if self.has_full_outfit:
            results += 'Contains full outfit for a brand\n'

        return results
        
class ExampleImpl006:
    def __init__(self):
        self.inventory = {}
        for type in types:
            for brand in brands:
                key = (type, brand)
                self.inventory[key] = starting_value

        self.is_valid = True

    def process_list(self, list_of_items):
        for item in list_of_items:
            self.process_one_item(item)

        self.check_has_full_outfit()
        return self.get_result_string()

    def process(self, filename):
        with open(filename, 'r') as file:
            try:
                list_of_items = json.load(file)
            except:
                self.is_valid = False
                list_of_items = []

        results = self.process_list(list_of_items)
        print(results)

    def process_one_item(self, item):
        type = item.get('type')
        brand = item.get('brand')
        quantity = item.get('quantity')

        if item.get('type') not in types:
            self.is_valid = False
            return

        if item.get('brand') not in brands:
            self.is_valid = False
            return

        try:
            quantity = int(quantity)
        except ValueError:
            self.is_valid = False
            return

        key = (type, brand)
        self.inventory[key] -= quantity
        if quantity >= starting_value:
            self.is_valid = False
            return

    def check_has_full_outfit(self):
        self.has_full_outfit = False
        for brand in brands:
            is_full_for_this_brand_so_far = True
            for type in types:
                key = (type, brand)
                if self.inventory[key] == starting_value:
                    is_full_for_this_brand_so_far = False

            if is_full_for_this_brand_so_far:
                self.has_full_outfit = True

    def get_result_string(self):
        if not self.is_valid:
            return 'Invalid input'

        results = 'Remaining inventory:\n'
        for type in types:
            for brand in brands:
                key = (type, brand)
                results += f'{type} {brand} {self.inventory[key]}\n'

        if self.has_full_outfit:
            results += 'Contains full outfit for a brand\n'

        return results

class ExampleImpl007:
    def __init__(self):
        self.inventory = {}
        for type in types:
            for brand in brands:
                key = (type, brand)
                self.inventory[key] = starting_value

        self.is_valid = True

    def process_list(self, list_of_items):
        for item in list_of_items:
            self.process_one_item(item)

        self.check_has_full_outfit()
        return self.get_result_string()

    def process(self, filename):
        with open(filename, 'r') as file:
            try:
                list_of_items = json.load(file)
            except:
                self.is_valid = False
                list_of_items = []

        results = self.process_list(list_of_items)
        print(results)

    def process_one_item(self, item):
        type = item.get('type')
        brand = item.get('brand')
        quantity = item.get('quantity')

        if item.get('type') not in types:
            self.is_valid = False
            return

        if item.get('brand') not in brands:
            self.is_valid = False
            return

        try:
            quantity = int(quantity)
        except ValueError:
            self.is_valid = False
            return

        key = (type, brand)
        self.inventory[key] -= quantity

    def check_has_full_outfit(self):
        self.has_full_outfit = False
        for brand in brands:
            is_full_for_this_brand_so_far = True
            for type in types:
                key = (type, brand)
                if self.inventory[key] == starting_value:
                    is_full_for_this_brand_so_far = False

            if is_full_for_this_brand_so_far:
                self.has_full_outfit = True

    def get_result_string(self):
        if not self.is_valid:
            return 'Invalid input'

        results = 'Remaining inventory:\n'
        for type in types:
            for brand in brands:
                key = (type, brand)
                results += f'{type} {brand} {self.inventory[key]}\n'

        if self.has_full_outfit:
            results += 'Contains full outfit for a brand\n'

        return results

class ExampleImpl008:
    def __init__(self):
        self.inventory = {}
        for type in types:
            for brand in brands:
                key = (type, brand)
                self.inventory[key] = starting_value

        self.is_valid = True

    def process_list(self, list_of_items):
        for item in list_of_items:
            self.process_one_item(item)

        self.check_has_full_outfit()
        return self.get_result_string()

    def process(self, filename):
        with open(filename, 'r') as file:
            try:
                list_of_items = json.load(file)
            except:
                self.is_valid = False
                list_of_items = []

        results = self.process_list(list_of_items)
        print(results)

    def process_one_item(self, item):
        type = item.get('type')
        brand = item.get('brand')
        quantity = item.get('quantity')

        if item.get('type') not in types:
            self.is_valid = False
            return

        if item.get('brand') not in brands:
            self.is_valid = False
            return

        try:
            quantity = int(quantity)
        except ValueError:
            self.is_valid = False
            return

        key = (type, brand)
        self.inventory[key] -= quantity
        if self.inventory[key] < 0:
            self.is_valid = False
            return

    def check_has_full_outfit(self):
        self.has_full_outfit = False
        for brand in brands:
            is_full_for_this_brand_so_far = True
            for type in types:
                key = (type, brand)
                if self.inventory[key] == starting_value:
                    is_full_for_this_brand_so_far = False

            if is_full_for_this_brand_so_far:
                self.has_full_outfit = True

    def get_result_string(self):
        if not self.is_valid:
            return 'Invalid input'

        results = 'Remaining inventory:\n'
        for type in types:
            for brand in brands:
                key = (type, brand)
                results += f'{type} {brand} {self.inventory[key]}\n'

        if self.has_full_outfit:
            results += 'Contains full outfit for a brand\n'

        return results
    
ExampleImpl008.expect_pass = True
    
class ExampleImpl009:
    def __init__(self):
        self.inventory = {}
        for type in types:
            for brand in brands:
                key = (type, brand)
                self.inventory[key] = starting_value

        self.is_valid = True

    def process_list(self, list_of_items):
        for item in list_of_items:
            self.process_one_item(item)

        self.check_has_full_outfit()
        return self.get_result_string()

    def process(self, filename):
        with open(filename, 'r') as file:
            try:
                list_of_items = json.load(file)
            except:
                self.is_valid = False
                list_of_items = []

        results = self.process_list(list_of_items)
        print(results)

    def process_one_item(self, item):
        type = item.get('type')
        brand = item.get('brand')
        quantity = item.get('quantity')

        if item.get('type') not in types:
            self.is_valid = False
            return

        if item.get('brand') not in brands:
            self.is_valid = False
            return

        try:
            quantity = int(quantity)
        except ValueError:
            self.is_valid = False
            return

        key = (type, brand)
        self.inventory[key] -= quantity
        if self.inventory[key] < 0:
            self.is_valid = False
            return

    def check_has_full_outfit(self):
        self.has_full_outfit = False
        articles_seen = {}
        for type in types:
            for key in self.inventory:
                type, brand = key
                articles_seen[type] = 1
        self.has_full_outfit = len(articles_seen) >= 3

    def get_result_string(self):
        if not self.is_valid:
            return 'Invalid input'

        results = 'Remaining inventory:\n'
        for type in types:
            for brand in brands:
                key = (type, brand)
                results += f'{type} {brand} {self.inventory[key]}\n'

        if self.has_full_outfit:
            results += 'Contains full outfit for a brand\n'

        return results

class ExampleImpl010:
    def __init__(self):
        self.inventory = {}
        for type in types:
            for brand in brands:
                key = (type, brand)
                self.inventory[key] = starting_value

        self.is_valid = True

    def process_list(self, list_of_items):
        for item in list_of_items:
            self.process_one_item(item)

        self.check_has_full_outfit()
        return self.get_result_string()

    def process(self, filename):
        with open(filename, 'r') as file:
            try:
                list_of_items = json.load(file)
            except:
                self.is_valid = False
                list_of_items = []

        results = self.process_list(list_of_items)
        print(results)

    def process_one_item(self, item):
        type = item.get('type')
        brand = item.get('brand')
        quantity = item.get('quantity')

        if item.get('type') not in types:
            self.is_valid = False
            return

        if item.get('brand') not in brands:
            self.is_valid = False
            return

        try:
            quantity = int(quantity)
        except ValueError:
            self.is_valid = False
            return

        key = (type, brand)
        self.inventory[key] -= quantity
        if self.inventory[key] < 0:
            self.is_valid = False
            return

    def check_has_full_outfit(self):
        self.has_full_outfit = len(self.inventory) >= 3

    def get_result_string(self):
        if not self.is_valid:
            return 'Invalid input'

        results = 'Remaining inventory:\n'
        for type in types:
            for brand in brands:
                key = (type, brand)
                results += f'{type} {brand} {self.inventory[key]}\n'

        if self.has_full_outfit:
            results += 'Contains full outfit for a brand\n'

        return results

class ExampleImpl011:
    def __init__(self):
        self.inventory = {}
        self.saw_key = {}
        for type in types:
            for brand in brands:
                key = (type, brand)
                self.inventory[key] = starting_value

        self.is_valid = True

    def process_list(self, list_of_items):
        for item in list_of_items:
            self.process_one_item(item)

        self.check_has_full_outfit()
        return self.get_result_string()

    def process(self, filename):
        with open(filename, 'r') as file:
            try:
                list_of_items = json.load(file)
            except:
                self.is_valid = False
                list_of_items = []

        results = self.process_list(list_of_items)
        print(results)

    def process_one_item(self, item):
        type = item.get('type')
        brand = item.get('brand')
        quantity = item.get('quantity')

        if item.get('type') not in types:
            self.is_valid = False
            return

        if item.get('brand') not in brands:
            self.is_valid = False
            return

        try:
            quantity = int(quantity)
        except ValueError:
            self.is_valid = False
            return

        key = (type, brand)
        self.saw_key[key] = True
        self.inventory[key] -= quantity
        if self.inventory[key] < 0:
            self.is_valid = False
            return

    def check_has_full_outfit(self):
        self.has_full_outfit = False
        for brand in brands:
            is_full_for_this_brand_so_far = True
            for type in types:
                key = (type, brand)
                if not saw_key.get(key):
                    is_full_for_this_brand_so_far = False

            if is_full_for_this_brand_so_far:
                self.has_full_outfit = True

    def get_result_string(self):
        if not self.is_valid:
            return 'Invalid input'

        results = 'Remaining inventory:\n'
        for type in types:
            for brand in brands:
                key = (type, brand)
                results += f'{type} {brand} {self.inventory[key]}\n'

        if self.has_full_outfit:
            results += 'Contains full outfit for a brand\n'

        return results

class ExampleImpl012:
    def __init__(self):
        self.inventory = {}
        for type in types:
            for brand in brands:
                key = (type, brand)
                self.inventory[key] = starting_value

        self.is_valid = True

    def process_list(self, list_of_items):
        for item in list_of_items:
            self.process_one_item(item)

        self.check_has_full_outfit()
        return self.get_result_string()

    def process(self, filename):
        with open(filename, 'r') as file:
            try:
                list_of_items = json.load(file)
            except:
                self.is_valid = False
                list_of_items = []

        results = self.process_list(list_of_items)
        print(results)

    def process_one_item(self, item):
        type = item.get('type')
        brand = item.get('brand')
        quantity = item.get('quantity')

        if item.get('type') not in types:
            self.is_valid = False
            return

        if item.get('brand') not in brands:
            self.is_valid = False
            return

        try:
            quantity = int(quantity)
        except ValueError:
            self.is_valid = False
            return

        key = (type, brand)
        self.inventory[key] -= quantity
        if self.inventory[key] < 0:
            self.is_valid = False
            return

    def check_has_full_outfit(self):
        self.has_full_outfit = False
        for brand in brands:
            is_full_for_this_brand_so_far = True
            for type in types:
                key = (type, brand)
                if self.inventory[key] == starting_value:
                    is_full_for_this_brand_so_far = False

            if is_full_for_this_brand_so_far:
                if self.has_full_outfit:
                    raise Exception("We don't support >1 complete outfit for some reason?")
                    
                self.has_full_outfit = True

    def get_result_string(self):
        if not self.is_valid:
            return 'Invalid input'

        results = 'Remaining inventory:\n'
        for type in types:
            for brand in brands:
                key = (type, brand)
                results += f'{type} {brand} {self.inventory[key]}\n'

        if self.has_full_outfit:
            results += 'Contains full outfit for a brand\n'

        return results

class ExampleImpl013:
    def __init__(self):
        self.inventory = {}
        for type in types:
            for brand in brands:
                key = (type, brand)
                self.inventory[key] = starting_value

        self.is_valid = True

    def process_list(self, list_of_items):
        for item in list_of_items:
            self.process_one_item(item)

        self.check_has_full_outfit()
        return self.get_result_string()

    def process(self, filename):
        with open(filename, 'r') as file:
            try:
                list_of_items = json.load(file)
            except:
                self.is_valid = False
                list_of_items = []

        results = self.process_list(list_of_items)
        print(results)

    def process_one_item(self, item):
        type = item.get('type')
        brand = item.get('brand')
        quantity = item.get('quantity')

        if item.get('type') not in types:
            self.is_valid = False
            return

        if item.get('brand') not in brands:
            self.is_valid = False
            return

        try:
            quantity = int(quantity)
        except ValueError:
            self.is_valid = False
            return

        key = (type, brand)
        self.inventory[key] += quantity
        if self.inventory[key] < 0:
            self.is_valid = False
            return

    def check_has_full_outfit(self):
        self.has_full_outfit = False
        for brand in brands:
            is_full_for_this_brand_so_far = True
            for type in types:
                key = (type, brand)
                if self.inventory[key] == starting_value:
                    is_full_for_this_brand_so_far = False

            if is_full_for_this_brand_so_far:
                self.has_full_outfit = True

    def get_result_string(self):
        if not self.is_valid:
            return 'Invalid input'

        results = 'Remaining inventory:\n'
        for type in types:
            for brand in brands:
                key = (type, brand)
                results += f'{type} {brand} {self.inventory[key]}\n'

        if self.has_full_outfit:
            results += 'Contains full outfit for a brand\n'

        return results

class ExampleImpl014:
    def __init__(self):
        self.inventory = {}
        for type in types:
            for brand in brands:
                key = (type, brand)
                self.inventory[key] = starting_value

        self.is_valid = True

    def process_list(self, list_of_items):
        for item in list_of_items:
            self.process_one_item(item)

        self.check_has_full_outfit()
        return self.get_result_string()

    def process(self, filename):
        with open(filename, 'r') as file:
            try:
                list_of_items = json.load(file)
            except:
                self.is_valid = False
                list_of_items = []

        results = self.process_list(list_of_items)
        print(results)

    def process_one_item(self, item):
        type = item.get('type')
        brand = item.get('brand')
        quantity = item.get('quantity')

        if item.get('type') not in types:
            self.is_valid = False
            return

        if item.get('brand') not in brands:
            self.is_valid = False
            return

        try:
            quantity = int(quantity)
        except ValueError:
            self.is_valid = False
            return

        key = (type, brand)
        self.inventory[key] -= quantity
        if self.inventory[key] < 0:
            self.is_valid = False
            return

    def check_has_full_outfit(self):
        self.has_full_outfit = False
        for brand in brands:
            is_full_for_this_brand_so_far = True
            for type in types:
                key = (type, brand)
                if self.inventory[key] == starting_value:
                    is_full_for_this_brand_so_far = False

            if is_full_for_this_brand_so_far:
                self.has_full_outfit = True

    def get_result_string(self):
        if not self.is_valid:
            return 'Invalid input'

        results = 'Remaining inventory:\n'
        for type in types:
            for brand in brands:
                if brand == 'fruche':
                    continue
                
                key = (type, brand)
                results += f'{type} {brand} {self.inventory[key]}\n'

        if self.has_full_outfit:
            results += 'Contains full outfit for a brand\n'

        return results

class ExampleImpl015:
    def __init__(self):
        self.inventory = {}
        for type in types:
            for brand in brands:
                key = (type, brand)
                self.inventory[key] = starting_value

        self.is_valid = True

    def process_list(self, list_of_items):
        for item in list_of_items:
            self.process_one_item(item)

        self.check_has_full_outfit()
        return self.get_result_string()

    def process(self, filename):
        with open(filename, 'r') as file:
            try:
                list_of_items = json.load(file)
            except:
                self.is_valid = False
                list_of_items = []

        results = self.process_list(list_of_items)
        print(results)

    def process_one_item(self, item):
        type = item.get('type')
        brand = item.get('brand')
        quantity = item.get('quantity')

        if item.get('type') not in types:
            self.is_valid = False
            return

        if item.get('brand') not in brands:
            self.is_valid = False
            return

        try:
            quantity = int(quantity)
        except ValueError:
            self.is_valid = False
            return

        key = (type, brand)
        self.inventory[key] -= quantity
        if self.inventory[key] < 0:
            self.is_valid = False
            return

    def check_has_full_outfit(self):
        self.has_full_outfit = False
        for brand in brands:
            is_full_for_this_brand_so_far = True
            for type in types:
                key = (type, brand)
                if self.inventory[key] == starting_value:
                    is_full_for_this_brand_so_far = False

            if is_full_for_this_brand_so_far:
                self.has_full_outfit = True

    def get_result_string(self):
        if not self.is_valid:
            return 'Invld inpt'

        results = 'Remaining inventory:\n'
        for type in types:
            for brand in brands:
                if brand == 'fruche':
                    continue

                key = (type, brand)
                results += f'{type} {brand} {self.inventory[key]}\n'

        if self.has_full_outfit:
            results += 'Contains full outfit for a brand\n'

        return results

classes = [
    ExampleImpl001,
    ExampleImpl002,
    ExampleImpl003,
    ExampleImpl004,
    ExampleImpl005,
    ExampleImpl006,
    ExampleImpl007,
    ExampleImpl008,
    ExampleImpl009,
    ExampleImpl010,
    ExampleImpl011,
    ExampleImpl012,
    ExampleImpl013,
    ExampleImpl014,
    ExampleImpl015,
    ]

def run_all_tests(Cls):
    test_store_order_processor.main.StoreOrderProcessor = Cls
    test_instance = test_store_order_processor.TestStoreOrderProcessor()
    for method_name in dir(test_instance):
        if method_name.startswith('test_'):
            try:
                getattr(test_instance, method_name)()
            except:
                raise AssertionError('test failed')

def test_tests():
    for Cls in classes:
        expect_tests_to_pass = 'expect_pass' in dir(Cls)
        try:
            run_all_tests(Cls)
            tests_passed = True
        except:
            tests_passed = False
        
        assert expect_tests_to_pass == tests_passed

if __name__ == '__main__':
    test_tests()
    
