import json

from implementations import store_order_processor

if __name__ == "__main__":
    try:
        processor = store_order_processor.StoreOrderProcessor()
        processor.process("example1.json")
    except Exception as e:
        print(f"Exception occurred: {e}")
