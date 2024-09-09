# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

import unittest
from brute_force_missing_addend_finder import BruteForceMissingAddendFinder
from hash_map_missing_addend_finder import HashMapMissingAddendFinder

class TestMissingAddendFinders(unittest.TestCase):
    def setUp(self):
        # expected missing_addends sorted in ascending order
        self.nums1, self.target1, self.expected_missing_addend_1, = [2,7,11,15], 9, [0,1]
        self.nums2, self.target2, self.expected_missing_addend_2 = [3,2,4], 6, [1,2]
        self.nums3, self.target3, self.expected_missing_addend_3 = [3,3], 6, [0,1]

    def test_brute_force_missing_addend_finder(self):
        brute_force_missing_addend_finder = BruteForceMissingAddendFinder()
        observed_missing_addend_1 = brute_force_missing_addend_finder.find_missing_addend(self.nums1, self.target1)
        observed_missing_addend_2 = brute_force_missing_addend_finder.find_missing_addend(self.nums2, self.target2)
        observed_missing_addend_3 = brute_force_missing_addend_finder.find_missing_addend(self.nums3, self.target3)

        self.assertEqual(sorted(observed_missing_addend_1), self.expected_missing_addend_1)
        self.assertEqual(sorted(observed_missing_addend_2), self.expected_missing_addend_2)
        self.assertEqual(sorted(observed_missing_addend_3), self.expected_missing_addend_3)

    def test_hash_map_missing_addend_finder(self):
        hash_map_missing_addend_finder = HashMapMissingAddendFinder()
        observed_missing_addend_1 = hash_map_missing_addend_finder.find_missing_addend(self.nums1, self.target1)
        observed_missing_addend_2 = hash_map_missing_addend_finder.find_missing_addend(self.nums2, self.target2)
        observed_missing_addend_3 = hash_map_missing_addend_finder.find_missing_addend(self.nums3, self.target3)

        self.assertEqual(sorted(observed_missing_addend_1), self.expected_missing_addend_1)
        self.assertEqual(sorted(observed_missing_addend_2), self.expected_missing_addend_2)
        self.assertEqual(sorted(observed_missing_addend_3), self.expected_missing_addend_3)

if __name__ == '__main__':
    unittest.main()