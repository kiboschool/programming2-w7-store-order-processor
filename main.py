
import json

from store_order_processor import StoreOrderProcessor

if __name__ == '__main__':
    processor = StoreOrderProcessor()
    processor.process('example1.json')
