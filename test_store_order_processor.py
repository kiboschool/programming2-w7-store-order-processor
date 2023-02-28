
import unittest
from implementations.store_order_processor import StoreOrderProcessor, StoreOrderProcessorException

'''Create an instance of the class currently being tested'''
def get_instance():
    return StoreOrderProcessor()

'''Check that the orderprocessor is working as intended'''
class TestStoreOrderProcessor(unittest.TestCase):
    def test_should_handle_invalid_type(self):
        with self.assertRaises(StoreOrderProcessorException):
            processor = get_instance()
            results = processor.process_list([
        {"type": "jacket", "brand": "fruche", "quantity": "2"},
        {"type": "slcks(typo)", "brand": "kente", "quantity": "1"}
    ])
        
    def test_should_handle_invalid_brand(self):
        with self.assertRaises(StoreOrderProcessorException):
            processor = get_instance()
            results = processor.process_list([
        {"type": "jacket", "brand": "fruche", "quantity": "2"},
        {"type": "slacks", "brand": "kent(typo)", "quantity": "1"}
    ])
        
    def test_should_handle_empty_string_quantity(self):
        with self.assertRaises(StoreOrderProcessorException):
            processor = get_instance()
            results = processor.process_list([
        {"type": "jacket", "brand": "fruche", "quantity": "2"},
        {"type": "slacks", "brand": "kente", "quantity": ""}
    ])
        
    def test_should_handle_alphabetic_quantity(self):
        with self.assertRaises(StoreOrderProcessorException):
            processor = get_instance()
            results = processor.process_list([
        {"type": "jacket", "brand": "fruche", "quantity": "2"},
        {"type": "slacks", "brand": "kente", "quantity": "abc"}
    ])
    
    def test_still_valid_if_inventory_leaves_one_remaining(self):
        processor = get_instance()
        results = processor.process_list([
    {"type": "jacket", "brand": "fruche", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "19"},
])
        assert_equal_ignoring_newlines(results, '''Remaining inventory:
jacket fruche 18
jacket onalaja 20
jacket kente 20
slacks fruche 20
slacks onalaja 20
slacks kente 1
pair_of_shoes fruche 20
pair_of_shoes onalaja 20
pair_of_shoes kente 20''')
        
    def test_still_valid_if_inventory_leaves_zero_remaining(self):
        # An inventory of 0 is valid.
        # This covers a common 'off-by-one' error where a bug might cause it to think an inventory of 0 is invalid
        processor = get_instance()
        results = processor.process_list([
    {"type": "jacket", "brand": "fruche", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "20"},
])
        assert_equal_ignoring_newlines(results, '''Remaining inventory:
jacket fruche 18
jacket onalaja 20
jacket kente 20
slacks fruche 20
slacks onalaja 20
slacks kente 0
pair_of_shoes fruche 20
pair_of_shoes onalaja 20
pair_of_shoes kente 20''')
    
    def test_not_valid_if_exceeds_inventory(self):
        with self.assertRaises(StoreOrderProcessorException):
            processor = get_instance()
            results = processor.process_list([
        {"type": "jacket", "brand": "fruche", "quantity": "2"},
        {"type": "slacks", "brand": "kente", "quantity": "22"},
    ])
    
    def test_should_not_be_valid_if_exceeds_inventory_across_multiple_rows(self):
        with self.assertRaises(StoreOrderProcessorException):
            processor = get_instance()
            results = processor.process_list([
        {"type": "jacket", "brand": "fruche", "quantity": "2"},
        {"type": "slacks", "brand": "kente", "quantity": "18"},
        {"type": "slacks", "brand": "kente", "quantity": "4"}
    ])
    
    
    def test_has_a_complete_outfit(self):
        processor = get_instance()
        results = processor.process_list([
    {"type": "jacket", "brand": "onalaja", "quantity": "2"},
    {"type": "slacks", "brand": "onalaja", "quantity": "2"},
    {"type": "pair_of_shoes", "brand": "onalaja", "quantity": "1"},
])
        assert_equal_ignoring_newlines(results, '''Remaining inventory:
jacket fruche 20
jacket onalaja 18
jacket kente 20
slacks fruche 20
slacks onalaja 18
slacks kente 20
pair_of_shoes fruche 20
pair_of_shoes onalaja 19
pair_of_shoes kente 20
Contains full outfit for a brand''')
        
    def test_should_not_say_full_outfit_regardless_of_brand(self):
        processor = get_instance()
        results = processor.process_list([
    {"type": "jacket", "brand": "fruche", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "2"},
    {"type": "pair_of_shoes", "brand": "kente", "quantity": "2"},
])
        assert_equal_ignoring_newlines(results, '''Remaining inventory:
jacket fruche 18
jacket onalaja 20
jacket kente 20
slacks fruche 20
slacks onalaja 20
slacks kente 18
pair_of_shoes fruche 20
pair_of_shoes onalaja 20
pair_of_shoes kente 18''')

    def test_should_not_say_full_outfit_if_there_are_2_slacks_and_1_jacket(self):
        processor = get_instance()
        results = processor.process_list([
    {"type": "jacket", "brand": "kente", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "2"},
])
        assert_equal_ignoring_newlines(results, '''Remaining inventory:
jacket fruche 20
jacket onalaja 20
jacket kente 18
slacks fruche 20
slacks onalaja 20
slacks kente 16
pair_of_shoes fruche 20
pair_of_shoes onalaja 20
pair_of_shoes kente 20''')

    def test_should_not_say_full_outfit_if_one_of_the_quantities_is_0(self):
        processor = get_instance()
        results = processor.process_list([
    {"type": "jacket", "brand": "kente", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "2"},
    {"type": "pair_of_shoes", "brand": "kente", "quantity": "0"},
])
        assert_equal_ignoring_newlines(results, '''Remaining inventory:
jacket fruche 20
jacket onalaja 20
jacket kente 18
slacks fruche 20
slacks onalaja 20
slacks kente 18
pair_of_shoes fruche 20
pair_of_shoes onalaja 20
pair_of_shoes kente 20''')


    def test_should_still_work_if_given_2_complete_outfits(self):
        processor = get_instance()
        results = processor.process_list([
    {"type": "jacket", "brand": "kente", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "2"},
    {"type": "pair_of_shoes", "brand": "kente", "quantity": "1"},
    {"type": "jacket", "brand": "onalaja", "quantity": "2"},
    {"type": "slacks", "brand": "onalaja", "quantity": "2"},
    {"type": "pair_of_shoes", "brand": "onalaja", "quantity": "1"},
])
        assert_equal_ignoring_newlines(results, '''Remaining inventory:
jacket fruche 20
jacket onalaja 18
jacket kente 18
slacks fruche 20
slacks onalaja 18
slacks kente 18
pair_of_shoes fruche 20
pair_of_shoes onalaja 19
pair_of_shoes kente 19
Contains full outfit for a brand''')


def assert_equal_ignoring_newlines(s1, s2):
    s1 = s1.replace('\r\n', '\n').strip()
    s2 = s2.replace('\r\n', '\n').strip()
    assert s1 == s2



if __name__ == "__main__":
    unittest.main()

