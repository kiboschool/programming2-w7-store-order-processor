import unittest
from implementations.store_order_processor import StoreOrderProcessor, StoreOrderProcessorException

'''Create an instance of the class currently being tested'''
def get_instance():
    return StoreOrderProcessor()

'''Check that the orderprocessor is working as intended'''
class TestStoreOrderProcessor(unittest.TestCase):
    # This test is already written for you.
    """Test that the StoreOrderProcessor raises a StoreOrderProcessorException exception when given an invalid type."""
    def test_should_handle_invalid_type(self):
        with self.assertRaises(StoreOrderProcessorException):
            processor = get_instance()
            results = processor.process_list([
                {"type": "jacket", "brand": "fruche", "quantity": "2"},
                {"type": "slcks(typo)", "brand": "kente", "quantity": "1"}
            ])
        
    # Now is your turn to write a test. Use the above example as a guide.
    """Test that the StoreOrderProcessor raises a StoreOrderProcessorException exception when given an invalid brand."""
    def test_should_handle_invalid_brand(self):
        # TODO: please write a test here
        # Just like the above test where we simulated the scenario where the type was invalid,
        # write your code to simulate the scenario where the brand is invalid
        raise NotImplementedError
        
    """Test that the StoreOrderProcessor raises a StoreOrderProcessorException exception when given an empty quantity."""
    def test_should_handle_empty_string_quantity(self):
        # TODO: please write a test here
        # Write your code to simulate the scenario where the quantity is an empty string
        raise NotImplementedError
        
    """Test that the StoreOrderProcessor raises a StoreOrderProcessorException exception when given a string quantity. """
    def test_should_handle_alphabetic_quantity(self):
        # TODO: please write a test here
        # Write your code to simulate the scenario where the quantity is a string instead of a number
        raise NotImplementedError
        
    # This test is already written for you.
    """ Tests that the StoreOrderProcessor correctly subtracts from the inventory. """
    def test_still_valid_if_inventory_leaves_one_remaining(self):
        processor = get_instance()
        results = processor.process_list([
            {"type": "jacket", "brand": "fruche", "quantity": "2"},
            {"type": "slacks", "brand": "kente", "quantity": "19"},
        ])
        assert_equal_ignoring_space(results, '''Remaining inventory:
                                                    jacket fruche 18
                                                    jacket onalaja 20
                                                    jacket kente 20
                                                    slacks fruche 20
                                                    slacks onalaja 20
                                                    slacks kente 1
                                                    pair_of_shoes fruche 20
                                                    pair_of_shoes onalaja 20
                                                    pair_of_shoes kente 20''')

    """Test that the StoreOrderProcessor correctly processes a list of items leaving zero remaining."""
    def test_still_valid_if_inventory_leaves_zero_remaining(self):
        # An inventory of 0 is valid.
        # TODO: please write a test here.
        # This covers a common 'off-by-one' error where the code treats an inventory of 0 as invalid, but really it should be valid
        raise NotImplementedError
    
    """Test that the StoreOrderProcessor raises a StoreOrderProcessorException exception when given an order that exceeds the inventory"""
    def test_not_valid_if_exceeds_inventory(self):
        # TODO: please write a test here
        # should raise StoreOrderProcessorException if there are more than the inventory.
        # your code should test the scenario where the quantity is greater than the inventory
        raise NotImplementedError
    
    # This test is already written for you.
    """Tests that the StoreOrderProcessor raises a StoreOrderProcessorException exception when given an order that exceeds the inventory, across separate items."""
    def test_should_not_be_valid_if_exceeds_inventory_across_multiple_rows(self):
        with self.assertRaises(StoreOrderProcessorException):
            processor = get_instance()
            results = processor.process_list([
                {"type": "jacket", "brand": "fruche", "quantity": "2"},
                {"type": "slacks", "brand": "kente", "quantity": "18"},
                {"type": "slacks", "brand": "kente", "quantity": "4"}
            ])
    
    # This test is already written for you.
    """ Tests that the StoreOrderProcessor correctly processes a list of items that contains a full outfit."""
    def test_has_a_complete_outfit(self):
        processor = get_instance()
        results = processor.process_list([
            {"type": "jacket", "brand": "onalaja", "quantity": "2"},
            {"type": "slacks", "brand": "onalaja", "quantity": "2"},
            {"type": "pair_of_shoes", "brand": "onalaja", "quantity": "1"},
        ])
        assert_equal_ignoring_space(results, '''Remaining inventory:
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
        
    """Test that the StoreOrderProcessor don't print the full outfit message if the items are not all the same brand."""
    def test_should_not_say_full_outfit_regardless_of_brand(self):
        # TODO: please write a test here
        # a full outfit must be only all for the same brand - if one of the items is a different brand, it doesn't count.
        raise NotImplementedError
        
    """Test that the StoreOrderProcessor don't print the full outfit message if there isn't an item of each type."""
    def test_should_not_say_full_outfit_if_there_are_2_slacks_and_1_jacket(self):
        # TODO: please write a test here
        # it's not a full outfit if there is no pair_of_shoes
        raise NotImplementedError

    """Test that the StoreOrderProcessor don't print the full outfit message if there isn't an item of each type."""
    def test_should_not_say_full_outfit_even_if_one_of_the_quantities_is_0(self):
        # TODO: please write a test here
        # Edge case where quantity is 0. It is not a full outfit if one of the items has quantity = 0!
        raise NotImplementedError
        
    """Test that the StoreOrderProcessor prints the full outfit message only one time 
    if given a list of items contains more than full outfit."""
    def test_should_still_work_if_given_2_complete_outfits(self):
        # TODO: write a test here
        raise NotImplementedError



def assert_equal_ignoring_space(s1, s2):
    # Skip whitespace and newlines
    s1 = s1.replace('\r', '').replace('\n', '').replace(' ', '').replace('\t', '')
    s2 = s2.replace('\r', '').replace('\n', '').replace(' ', '').replace('\t', '')
    if s1 != s2:
        print('First string:', s1)
        print('Second string:', s2)
        
    assert s1 == s2



if __name__ == "__main__":
    unittest.main()

