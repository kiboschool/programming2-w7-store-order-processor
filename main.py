import json

types = ['jacket', 'slacks', 'pair_of_shoes']
brands = ['fruche', 'onalaja', 'kente']
starting_value = 20

class StoreOrderProcessor:
    def __init__(self):
        # please write your intitialization code here.
        pass
    
    def process(self, filename):
        with open(filename, 'r') as file:
            list_of_items = json.load(file)
            
        results = self.process_list(list_of_items)
        print(results)
        
    def process_list(self, list_of_items):
        # please write your processing code here,
        # it should loop through list_of_items and process each item.
        # helper methods are fine, and recommended.
        
        results = 'Remaining inventory:'
        # then, add the inventory text to the results string.
        
        return results
    
if __name__ == '__main__':
    processor = StoreOrderProcessor()
    processor.process('example1.json')
    