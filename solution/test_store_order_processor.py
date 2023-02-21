import unittest
import main

def assertEqualStrModuloNewlines(s1, s2):
    s1 = s1.replace('\r\n', '\n').strip()
    s2 = s2.replace('\r\n', '\n').strip()
    if s1 != s2:
        print(s1+'---')
        print(s2+'---')
    assert s1==s2

class TestStoreOrderProcessor(unittest.TestCase):
    def test_crashes_on_invalid_type(self):
        processor = main.StoreOrderProcessor()
        results = processor.process_list([
    {"type": "jacket", "brand": "fruche", "quantity": "2"},
    {"type": "slcks(typo)", "brand": "kente", "quantity": "1"}
])
        assert results.strip() == 'Invalid input'
        
    def test_crashes_on_invalid_brand(self):
        processor = main.StoreOrderProcessor()
        results = processor.process_list([
    {"type": "jacket", "brand": "fruche", "quantity": "2"},
    {"type": "slacks", "brand": "kent-typo", "quantity": "1"}
])
        assert results.strip() == 'Invalid input'
        
    def test_crashes_on_empty_string_or_None_quantity(self):
        processor = main.StoreOrderProcessor()
        results = processor.process_list([
    {"type": "jacket", "brand": "fruche", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": ""}
])
        assert results.strip() == 'Invalid input'
        
    def test_crashes_on_alphabetic_quantity(self):
        processor = main.StoreOrderProcessor()
        results = processor.process_list([
    {"type": "jacket", "brand": "fruche", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "abc"}
])
        assert results.strip() == 'Invalid input'
        
    def test_still_valid_if_exceeds_inventory_across_multiple_rows(self):
        processor = main.StoreOrderProcessor()
        results = processor.process_list([
    {"type": "jacket", "brand": "fruche", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "18"},
    {"type": "slacks", "brand": "kente", "quantity": "4"}
])
        assert results.strip() == 'Invalid input'
        
    def test_off_by_one_error(self):
        processor = main.StoreOrderProcessor()
        results = processor.process_list([
    {"type": "jacket", "brand": "fruche", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "20"},
])
        assertEqualStrModuloNewlines(results, '''Remaining inventory:
jacket fruche 18
jacket onalaja 20
jacket kente 20
slacks fruche 20
slacks onalaja 20
slacks kente 0
pair_of_shoes fruche 20
pair_of_shoes onalaja 20
pair_of_shoes kente 20''')
    
    def test_still_valid_if_exceeds_inventory(self):
        processor = main.StoreOrderProcessor()
        results = processor.process_list([
    {"type": "jacket", "brand": "fruche", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "22"},
])
        assert results.strip() == 'Invalid input'
        
    def test_says_full_outfit_regardless_of_brand(self):
        processor = main.StoreOrderProcessor()
        results = processor.process_list([
    {"type": "jacket", "brand": "fruche", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "2"},
    {"type": "pair_of_shoes", "brand": "kente", "quantity": "2"},
])
        assertEqualStrModuloNewlines(results, '''Remaining inventory:
jacket fruche 18
jacket onalaja 20
jacket kente 20
slacks fruche 20
slacks onalaja 20
slacks kente 18
pair_of_shoes fruche 20
pair_of_shoes onalaja 20
pair_of_shoes kente 18''')

    def test_says_full_outfit_if_there_are_2_slacks_and_1_jacket(self):
        processor = main.StoreOrderProcessor()
        results = processor.process_list([
    {"type": "jacket", "brand": "kente", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "2"},
])
        assertEqualStrModuloNewlines(results, '''Remaining inventory:
jacket fruche 20
jacket onalaja 20
jacket kente 18
slacks fruche 20
slacks onalaja 20
slacks kente 16
pair_of_shoes fruche 20
pair_of_shoes onalaja 20
pair_of_shoes kente 20''')

    def test_says_full_outfit_even_if_one_of_the_quantities_is_0(self):
        processor = main.StoreOrderProcessor()
        results = processor.process_list([
    {"type": "jacket", "brand": "kente", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "2"},
    {"type": "pair_of_shoes", "brand": "kente", "quantity": "0"},
])
        assertEqualStrModuloNewlines(results, '''Remaining inventory:
jacket fruche 20
jacket onalaja 20
jacket kente 18
slacks fruche 20
slacks onalaja 20
slacks kente 18
pair_of_shoes fruche 20
pair_of_shoes onalaja 20
pair_of_shoes kente 20''')

    def test_has_a_complete_outfit_(self):
        processor = main.StoreOrderProcessor()
        results = processor.process_list([
    {"type": "jacket", "brand": "onalaja", "quantity": "2"},
    {"type": "slacks", "brand": "onalaja", "quantity": "2"},
    {"type": "pair_of_shoes", "brand": "onalaja", "quantity": "1"},
])
        assertEqualStrModuloNewlines(results, '''Remaining inventory:
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

    def test_crashes_if_given_2_complete_outfits_(self):
        processor = main.StoreOrderProcessor()
        results = processor.process_list([
    {"type": "jacket", "brand": "kente", "quantity": "2"},
    {"type": "slacks", "brand": "kente", "quantity": "2"},
    {"type": "pair_of_shoes", "brand": "kente", "quantity": "1"},
    {"type": "jacket", "brand": "onalaja", "quantity": "2"},
    {"type": "slacks", "brand": "onalaja", "quantity": "2"},
    {"type": "pair_of_shoes", "brand": "onalaja", "quantity": "1"},
])
        assertEqualStrModuloNewlines(results, '''Remaining inventory:
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







if __name__ == "__main__":
    unittest.main()


