
import json

from store_order_processor import StoreOrderProcessor

if __name__ == '__main__':
    try:
        processor = StoreOrderProcessor()
        processor.process('example1.json')
    except Exception as e:
        print(f'Exception occurred: {e}')

