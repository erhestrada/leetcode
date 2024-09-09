# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# time complexity O(n^2), looking through every combination of elements
class BruteForceMissingAddendFinder():
    def find_missing_addend(self, nums, target):
        for i in range(len(nums) - 1):
            first_addend = nums[i]
            for j in range(i+1, len(nums)):
                second_addend = nums[j]
                sum_ = first_addend + second_addend
                if sum_ == target:
                    return [i, j]
        return []