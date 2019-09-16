# 1. Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# o(n^2) solution because might have to check through all of both arrays
# throws error with input [3,2,4], 6
# output is [0,0], expected output [1,2]

  def twoSum(self, nums, target):
    # for loop in python, replaced nums with a range going from
    # the first element to the last
    for first in range(0,len(nums)):
      # each input only has one solution and no repeat elements
      # so the second pair we check for has to be greater than the first
      # don't need to check for elements that we already passed over
      # second = first + 1
      # gets overwritting with second for in loop
      for second in range(first + 1,len(nums)):
        if (nums[first] + nums[second] == target):
          return [first, second]

# faster time strat
# iterate through nums passing the difference between
# the 'num' and the target into a dictionary (python object equivalent)
# during nums loop, if num is a key in the dictionary
# you now have both indices of numbers that sum to target
