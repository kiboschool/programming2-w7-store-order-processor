
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
        
    def processImpl(self, order_list):
        for item in order_list:
            self.process_item(item)
            
        hasFullOutfit = self.checkHasFullOutfit()
        return hasFullOutfit
        
    def processItem(self, item):
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
        hasFull = False
        for brand in brands:
            isFullForThisBrand = True
    
            
    