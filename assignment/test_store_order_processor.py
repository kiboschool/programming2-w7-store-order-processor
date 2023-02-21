import unittest
import main


class TestStoreOrderProcessor(unittest.TestCase):
    def test_one_jacket_two_slacks(self):
        player = main.StoreOrderProcessor(songs)
        assert player.current_state() == "Paused"
    
    # todo: please add many more tests here!
    # (but leave the structure of this file as-is)
    
    # you must check for all features, including cases where the order would run out of inventory,
    # and including cases where there is a complete outfit for a brand,
    # and checking that invalid input will cause the output to be 'Invalid input'


if __name__ == "__main__":
    unittest.main()
