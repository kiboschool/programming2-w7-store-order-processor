
import unittest
from store_order_processor import StoreOrderProcessor


class TestStoreOrderProcessor(unittest.TestCase):
    types = []
    brands = []
    starting_value = 0

    def test_valid_two_brands_order(self):
        processor = StoreOrderProcessor()
        results = processor.process_list([
            {"type": "jacket", "brand": "fruche", "quantity": "2"},
            {"type": "slacks", "brand": "kente", "quantity": "1"}
        ])
        assertEqualStrModuloNewlines(results, '''Remaining inventory:
jacket fruche 18
jacket onalaja 20
jacket kente 20
slacks fruche 20
slacks onalaja 20
slacks kente 19
pair_of_shoes fruche 20
pair_of_shoes onalaja 20
pair_of_shoes kente 20''')

    # test another valid order
    # TODO Students to implement this test
    def test_valid_three_brands_order(self):
        processor = StoreOrderProcessor()
        results = processor.process_list([
            {"type": "jacket", "brand": "fruche", "quantity": "4"},
            {"type": "slacks", "brand": "kente", "quantity": "3"},
            {"type": "pair_of_shoes", "brand": "fruche", "quantity": "11"}
        ])
        assertEqualStrModuloNewlines(results, '''Remaining inventory:
jacket fruche 16
jacket onalaja 20
jacket kente 20
slacks fruche 20
slacks onalaja 20
slacks kente 17
pair_of_shoes fruche 9
pair_of_shoes onalaja 20
pair_of_shoes kente 20''')

    def test_types(self):
        TestStoreOrderProcessor.types = StoreOrderProcessor.types
        TestStoreOrderProcessor.starting_value = StoreOrderProcessor.starting_value

        assert TestStoreOrderProcessor.types == [
            'jacket', 'slacks', 'pair_of_shoes']

    # TODO Students to implement this test
    def test_brands(self):
        TestStoreOrderProcessor.brands = StoreOrderProcessor.brands
        assert TestStoreOrderProcessor.brands == ['fruche', 'onalaja', 'kente']

    def test_crashes_on_invalid_type(self):
        with self.assertRaises(Exception) as context:
            processor = StoreOrderProcessor()
            processor.process_list([
                {"type": "jacket", "brand": "fruche", "quantity": "2"},
                {"type": "slacksiyat", "brand": "kente", "quantity": "1"}
            ])

            self.assertTrue('Invalid item type' in str(context.exception))

    # TODO Students to implement this test
    def test_crashes_on_invalid_brand(self):

        with self.assertRaises(Exception) as context:
            processor = StoreOrderProcessor()
            processor.process_list([
                {"type": "jacket", "brand": "fruche", "quantity": "2"},
                {"type": "slacks", "brand": "kent-typo", "quantity": "1"}
            ])

            self.assertTrue('Invalid item brand' in str(context.exception))

    def test_crashes_on_empty_string_or_None_quantity(self):
        with self.assertRaises(Exception) as context:
            processor = StoreOrderProcessor()
            processor.process_list([
                {"type": "jacket", "brand": "fruche", "quantity": "2"},
                {"type": "slacks", "brand": "kente", "quantity": ""}
            ])

            self.assertTrue('Invalid input' in str(context.exception))

    # TODO Students to implement this test
    def test_crashes_on_alphabetic_quantity(self):
        with self.assertRaises(Exception) as context:
            processor = StoreOrderProcessor()
            processor.process_list([
                {"type": "jacket", "brand": "fruche", "quantity": "2"},
                {"type": "slacks", "brand": "kente", "quantity": "abc"}
            ])

            self.assertTrue('Invalid input' in str(context.exception))

    # test has a full outfit of jacket, slacks, and shoes

    def test_full_outfit_fruche(self):
        processor = StoreOrderProcessor()
        results = processor.process_list([
            {"type": "jacket", "brand": "onalaja", "quantity": "2"},
            {"type": "slacks", "brand": "kente", "quantity": "12"},
        ])
        assert processor.check_has_full_outfit('fruche') == True

    # TODO Students to implement this test
    def test_full_outfit_fruche_false(self):
        processor = StoreOrderProcessor()
        results = processor.process_list([
            {"type": "jacket", "brand": "fruche", "quantity": "2"},
            {"type": "slacks", "brand": "kente", "quantity": "2"},
            {"type": "slacks", "brand": "fruche", "quantity": "1"},
        ])
        self.assertFalse(processor.check_has_full_outfit('fruche'))

    def test_still_valid_if_exceeds_inventory(self):
        with self.assertRaises(Exception) as context:
            processor = StoreOrderProcessor()
            processor.process_list([
                {"type": "jacket", "brand": "fruche", "quantity": "2"},
                {"type": "slacks", "brand": "kente", "quantity": "22"},
            ])

            self.assertTrue('Not enough in stock' in str(context.exception))

    # TODO Students to implement this test
    def test_out_of_stock_inventory(self):
        with self.assertRaises(Exception) as context:
            processor = StoreOrderProcessor()
            processor.process_list([
                {"type": "jacket", "brand": "fruche", "quantity": "2"},
                {"type": "slacks", "brand": "kente", "quantity": "20"},
                {"type": "slacks", "brand": "kente", "quantity": "1"},
            ])

            self.assertTrue('Out of stock' in str(context.exception))


def assertEqualStrModuloNewlines(s1, s2):
    s1 = s1.replace('\r\n', '\n').strip()
    s2 = s2.replace('\r\n', '\n').strip()
    assert s1 == s2


if __name__ == "__main__":
    unittest.main()
