import json

types = ['jacket', 'slacks', 'pair_of_shoes']
brands = ['Fruche', 'Onalaja', 'Kente']
starting_value = 20

class StoreOrderProcessor:
    def __init__(self):
        self.inventory = {}
        for type in types:
            for brand in brands:
                key = (type, brand)
                self.inventory[key] = starting_value
        
        self.isValid = True
    
    def process(self, filename):
        with open(filename, 'r') as file:
            list_of_items = json.load(file)
            self.processEachItem(list_of_items)
            
        results = self.getResults()
        print(results)
        
    def processEachItem(self, list_of_items):
        for item in list_of_items:
            self.processOneItem(item)
        self.checkHasFullOutfit()
        
    def processOneItem(self, item):
        if item.get('type') not in types:
            self.isValid = False
            return
        if item.get('brand') not in brands:
            self.isValid = False
            return
        try:
            quantity = int(item.get('quantity'))
        except ValueError:
            self.isValid = False
            return
        
        key = (type, brand)
        self.inventory[key] -= quanitity
        if self.inventory[key] < 0:
            self.isValid = False
            return
    
    def checkHasFullOutfit(self):
        self.hasFullOutfit = False
        for brand in brands:
            isFullForThisBrandSoFar = True
            for type in types:
                key = (type, brand)
                if self.inventory[key] == starting_value:
                    isFullForThisBrandSoFar = False
 
            if isFullForThisBrandSoFar:
                self.hasFullOutfit = True
        
    def getResults(self):
        if not self.isValid:
            return 'Invalid input'
            
        results = 'Remaining inventory:\n'
        for type in types:
            for brand in brands:
                key = (type, brand)
                results += f'{type} {brand} {self.inventory[key]}\n'
        
        if self.hasFullOutfit:
            results += 'Contains full outfit for brand'
        
        return results
        

                
            
    