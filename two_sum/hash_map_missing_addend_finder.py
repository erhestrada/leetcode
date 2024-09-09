# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# time complexity: O(n), space complexity: O(n)
class HashMapMissingAddendFinder():
    def find_missing_addend(self, nums, target):
        hash_map_so_far = {}
        for first_addend_index, first_addend in enumerate(nums):
            difference = target - first_addend
            if difference in hash_map_so_far:
                second_addend_index = hash_map_so_far[difference]
                return [first_addend_index, second_addend_index]
            hash_map_so_far[first_addend] = first_addend_index
        return []    