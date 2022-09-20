#import the testing framework and the actual functions you want to test
import unittest
from best_json_search import *
from test_data import *

# the triple apostrophe statements are returned upon an error, basically they are pre-written error messages
class json_search_test(unittest.TestCase):
    """test module to test search function in 'recursive_json_search' """

    def test_search_found(self):
        """key should be found, return list should not be empty"""
        self.assertTrue([]!=json_search(key1,data))

    def test_search_not_found(self):
        """key should not be found, should return an empty list"""
        self.assertTrue([]==json_search(key2,data))
    
    def test_is_a_list(self):
        """should return a list"""
        self.assertIsInstance(json_search(key1,data),list)

if __name__ == '__main__':
    unittest.main()