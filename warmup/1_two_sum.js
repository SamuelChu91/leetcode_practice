// # 1. Two Sum
// # Given an array of integers, return indices of the two numbers such that they add up to a specific target.

// # You may assume that each input would have exactly one solution, and you may not use the same element twice.

// # Example:

// # Given nums = [2, 7, 11, 15], target = 9,

// # Because nums[0] + nums[1] = 2 + 7 = 9,
// # return [0, 1].

// for some reason the same algorithm for this naive solution
// works in javascript but throws error in python on leetcode

const twosum = (nums, target) => {
  for (let first = 0; first < nums.length; first += 1) {
    for (let second = first + 1; second < nums.length; second += 1) {
      if (nums[first] + nums[second] == target) {
        return [first, second];
      }
    }
  }
}

const test = [3,2,4];
const target = 6;

console.log(twosum(test, target));