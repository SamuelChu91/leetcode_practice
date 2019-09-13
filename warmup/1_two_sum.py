# 1. Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# o(n^2) solution because might have to check through all of both arrays

  def twoSum(self, nums, target):
    # for loop in python, replaced nums with a range going from
    # the first element to the last
    for first in range(0,len(nums)):
      # each input only has one solution and no repeat elements
      # so the second pair we check for has to be greater than the first
      # don't need to check for elements that we already passed over
      second = first + 1
      for second in range(0,len(nums)):
        if (nums[first] + nums[second] == target):
          return [first, second]
