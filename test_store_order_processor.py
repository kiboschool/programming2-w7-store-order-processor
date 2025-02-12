import unittest
from implementations.store_order_processor import (
    StoreOrderProcessor,
    StoreOrderProcessorException,
)


#########
# Helper Functions
#########


def get_instance():
    """Create an instance of the class currently being tested"""
    return StoreOrderProcessor()


def assert_equal_ignoring_space(s1, s2):
    """Check if two strings are equal, but ignore differences in whitespace"""
    # Skip whitespace and newlines
    s1 = s1.replace("\r", "").replace("\n", "").replace(" ", "").replace("\t", "")
    s2 = s2.replace("\r", "").replace("\n", "").replace(" ", "").replace("\t", "")
    if s1 != s2:
        print("First string:", s1)
        print("Second string:", s2)

    assert s1 == s2


#############
# OrderProcessor Tests
#############


class TestStoreOrderProcessor(unittest.TestCase):
    # This test is already written for you.
    def test_processing_order_reduces_inventory(self):
        # This test processes an order and checks that the inventory is reduced
        processor = get_instance()
        assert processor.get_current_inventory("jacket", "fruche") == 20
        processor.process_list([{"type": "jacket", "brand": "fruche", "quantity": "2"}])
        assert processor.get_current_inventory("jacket", "fruche") == 18

    def test_processing_multiple_orders_reduces_inventory(self):
        # This test should check that processing a list of orders reduces the inventory for each of the items
        processor = get_instance()
        assert processor.get_current_inventory("jacket", "fruche") == 20
        assert processor.get_current_inventory("slacks", "kente") == 20
        processor.process_list(
            [
                {"type": "jacket", "brand": "fruche", "quantity": "2"},
                {"type": "slacks", "brand": "kente", "quantity": "19"},
            ]
        )
        # TODO: write the assertions here to check that the inventory is reduced correctly

    # This test is already written for you.
    def test_processes_order_and_displays_output(self):
        processor = get_instance()
        results = processor.process_list(
            [{"type": "jacket", "brand": "fruche", "quantity": "2"}]
        )
        assert_equal_ignoring_space(
            results,
            """Remaining inventory:
                                                    jacket fruche 18
                                                    jacket onalaja 20
                                                    jacket kente 20
                                                    slacks fruche 20
                                                    slacks onalaja 20
                                                    slacks kente 20
                                                    pair_of_shoes fruche 20
                                                    pair_of_shoes onalaja 20
                                                    pair_of_shoes kente 20""",
        )

    # This test is already written for you.
    def test_still_valid_if_inventory_leaves_one_remaining(self):
        """Tests that the StoreOrderProcessor correctly subtracts from the inventory."""
        processor = get_instance()
        results = processor.process_list(
            [
                {"type": "jacket", "brand": "fruche", "quantity": "2"},
                {"type": "slacks", "brand": "kente", "quantity": "19"},
            ]
        )
        assert_equal_ignoring_space(
            results,
            """Remaining inventory:
                                                    jacket fruche 18
                                                    jacket onalaja 20
                                                    jacket kente 20
                                                    slacks fruche 20
                                                    slacks onalaja 20
                                                    slacks kente 1
                                                    pair_of_shoes fruche 20
                                                    pair_of_shoes onalaja 20
                                                    pair_of_shoes kente 20""",
        )

    def test_still_valid_if_inventory_leaves_zero_remaining(self):
        """Test that the StoreOrderProcessor correctly processes a list of items leaving zero remaining."""
        # An inventory of 0 is valid.
        # TODO: write a test here.
        # This covers a common 'off-by-one' error where the code treats an inventory of 0 as invalid, but really it should be valid
        raise NotImplementedError

    # This test is already written for you.
    def test_raises_error_if_orders_exceed_inventory(self):
        """Tests that the StoreOrderProcessor raises a StoreOrderProcessorException exception when given an order that exceeds the inventory, across separate items."""
        with self.assertRaises(StoreOrderProcessorException):
            processor = get_instance()
            processor.process_list(
                [
                    {"type": "jacket", "brand": "fruche", "quantity": "2"},
                    {"type": "slacks", "brand": "kente", "quantity": "18"},
                    {"type": "slacks", "brand": "kente", "quantity": "4"},
                ]
            )

    def test_not_valid_if_exceeds_inventory(self):
        """Test that the StoreOrderProcessor raises a StoreOrderProcessorException exception when given an order that exceeds the inventory"""
        # should raise StoreOrderProcessorException if the inventory goes below zero
        # TODO: test the scenario where the quantity is greater than the inventory
        raise NotImplementedError

    # This test is already written for you.
    def test_should_handle_invalid_type(self):
        """Test that the StoreOrderProcessor raises a StoreOrderProcessorException exception when given an invalid type."""
        with self.assertRaises(StoreOrderProcessorException):
            processor = get_instance()
            results = processor.process_list(
                [
                    {"type": "jacket", "brand": "fruche", "quantity": "2"},
                    {"type": "slcks(typo)", "brand": "kente", "quantity": "1"},
                ]
            )

    # Now is your turn to write a test. Use the above example as a guide.
    def test_should_handle_invalid_brand(self):
        """Test that the StoreOrderProcessor raises a StoreOrderProcessorException exception when given an invalid brand."""
        # TODO: write a test here
        # Just like the above test where we simulated the scenario where the type was invalid,
        # write your code to simulate the scenario where the brand is invalid
        raise NotImplementedError

    def test_should_handle_empty_string_quantity(self):
        """Test that the StoreOrderProcessor raises a StoreOrderProcessorException exception when given an empty quantity."""
        # TODO: write a test here
        # Write your code to simulate the scenario where the quantity is an empty string
        raise NotImplementedError

    def test_should_handle_alphabetic_quantity(self):
        """Test that the StoreOrderProcessor raises a StoreOrderProcessorException exception when given a string quantity."""
        # TODO: write a test here
        # Write your code to simulate the scenario where the quantity is a string instead of a number
        raise NotImplementedError


if __name__ == "__main__":
    unittest.main()
