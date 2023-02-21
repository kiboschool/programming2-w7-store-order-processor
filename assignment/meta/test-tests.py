
starting_value = 20

# the 'explanation' comments won't be in the copy of this file given to students

# this is a long file so students can't cheat by copying a working file in from here.
# (but no need to make it truly hidden)
# it's ok that a student could complete the first part of the assignment by copying a class here
# and fixing it, if they do that more power to them :p
# could put a working class and inherit, but then students could see this

class Broken001: # explanation: crashes on invalid type
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


class Broken002: # explanation: crashes on invalid brand
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

class Broken003: # explanation: crashes on empty string or None quantity
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

class Broken004: # explanation: crashes on alphabetic quantity
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

class Broken005: # explanation: still valid if exceeds inventory across multiple rows
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
        
class Broken006: # explanation: off-by-one-error, says invalid too early
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

class Broken007: # explanation: still valid if exceeds inventory
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

class Broken008: # explanation: says full outfit regardless of brand
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

class Broken009: # explanation: says full outfit if there are 2 slacks and 1 jacket
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

class Broken010: # explanation: says full outfit even if one of the quantities is 0
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

class Broken011: # explanation: crashes if given 2 complete outfits (less realistic, but student should cover this in the tests)
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

class Broken012: # explanation: gives wrong inventory-adds instead of subtracts
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

class Broken013: # explanation: gives wrong inventory-misses one of the brands
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

class Broken014: # explanation: gives wrong inventory-previous and misspells Invalid input
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




def test_tests():
    
