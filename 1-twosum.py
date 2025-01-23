# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?



from typing import List


def testCases():
    testClass = Solution()
    assert(sorted(testClass.twoSum( nums = [3,2,4], target = 6 )) == sorted([1,2]))
    assert(sorted(testClass.twoSum( nums = [2,7,11,15], target = 9 )) == sorted([0,1]))
    assert(sorted(testClass.twoSum( nums = [3,3], target = 6 )) == sorted([0,1]))
    print("All Test Cases Passed!")
    
"""


    @type  nums: List[int]
    @param nums: List of numbers
    @type  target: int
    @param b: target number to find the constiuents of in nums list
    @rtype:   List
    @return:  List of 2 numbers with each number representing the indices of numbers in list nums that add up to target value


"""
class Solution:

    def __init__(self):
        pass

    # First Iteration (Quick solution)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for o in list(range(len(nums)))[:i] :
    #             if nums[i] + nums[o] == target:
    #                 return [i,o]

    # Second Iteration (Attempt at memory efficiency)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     i = 0
    #     o = 0
    #     while(i < len(nums)):
    #         o = i+1
    #         while(o < len(nums)):
    #             if nums[i] + nums[o] == target:
    #                 return [i,o]
    #             o+=1
    #         i+=1

    # Third Iteration (Hashtable Implementation O(n))
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}

        for i in range(len(nums)):
            if hashTable.get(target-nums[i]) != None:
                return [i, hashTable.get(target-nums[i])]
            hashTable[nums[i]] = i


testCases()