import unittest
import main


class TestStoreOrderProcessor(unittest.TestCase):
    def test_example(self):
        processor = main.StoreOrderProcessor()
        # ... add a test here
    
    # todo: please add many tests here!
    # The tests can call into either the main process_list() method,
    #  or a helper method you have added.
    
    # You should check for all features,
    # including cases where the order would run out of inventory,
    # including cases where there is a complete outfit for a brand,
    # and checking that invalid input will cause the output to be 'Invalid input'


if __name__ == "__main__":
    unittest.main()

