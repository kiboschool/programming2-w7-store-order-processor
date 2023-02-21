import json

types = ['jacket', 'slacks', 'pair_of_shoes']
brands = ['fruche', 'onalaja', 'kente']
starting_value = 20

class store_order_processor:
    def __init__(self):
        self.inventory = {}
        for type in types:
            for brand in brands:
                key = (type, brand)
                self.inventory[key] = starting_value
        
        self.is_valid = true
    
    def process(self, filename):
        with open(filename, 'r') as file:
            list_of_items = json.load(file)
            self.process_each_item(list_of_items)
            
        results = self.get_results()
        print(results)
        
    def process_each_item(self, list_of_items):
        for item in list_of_items:
            self.process_one_item(item)
        self.check_has_full_outfit()
        
    def process_one_item(self, item):
        if item.get('type') not in types:
            self.is_valid = false
            return
        if item.get('brand') not in brands:
            self.is_valid = false
            return
        try:
            quantity = int(item.get('quantity'))
        except value_error:
            self.is_valid = false
            return
        
        key = (type, brand)
        self.inventory[key] -= quanitity
        if self.inventory[key] < 0:
            self.is_valid = false
            return
    
    def check_has_full_outfit(self):
        self.has_full_outfit = false
        for brand in brands:
            is_full_for_this_brand_so_far = true
            for type in types:
                key = (type, brand)
                if self.inventory[key] == starting_value:
                    is_full_for_this_brand_so_far = false
 
            if is_full_for_this_brand_so_far:
                self.has_full_outfit = true
        
    def get_results(self):
        if not self.is_valid:
            return 'invalid input'
            
        results = 'remaining inventory:'
        for type in types:
            for brand in brands:
                key = (type, brand)
                results += f'{type} {brand} {self.inventory[key]}'
        
        if self.has_full_outfit:
            results += 'contains full outfit for brand'
        
        return results
        

                
            
    
