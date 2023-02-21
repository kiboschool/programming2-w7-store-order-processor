import json

types = ['jacket', 'slacks', 'pair_of_shoes']
brands = ['fruche', 'onalaja', 'kente']
starting_value = 20


class StoreOrderProcessor:
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
        


if __name__ == '__main__':
    processor = StoreOrderProcessor()
    processor.process('example3.json')
    