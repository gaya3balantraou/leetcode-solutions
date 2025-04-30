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
 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # This dictionary stores numbers we've seen so far along with their indices

        # Loop through each number in the list by index
        for i in range(len(nums)):
            diff = target - nums[i]  # Calculate the number we need to find to reach the target

            # If we've already seen the number needed to reach the target, we found our pair
            if diff in seen:
                return [seen[diff], i]  # Return the indices of the two numbers that add up to the target

            # Otherwise, store the current number and its index in the dictionary
            seen[nums[i]] = i

# Explanation
# nums = [3, 1, 4, 2]
# target = 6

# Iteration 1:
# i = 0, nums[i] = 3, so diff = 6 - 3 = 3
# 3 not in seen, so store 3:0
# seen → {3: 0}

# Iteration 2:
# i = 1, nums[i] = 1, so diff = 6 - 1 = 5
# 5 not in seen, so store 1:1
# seen → {3: 0, 1: 1}

# Iteration 3:
# i = 2, nums[i] = 4, so diff = 6 - 4 = 2
# 2 not in seen, so store 4:2
# seen → {3: 0, 1: 1, 4: 2}

# Iteration 4:
# i = 3, nums[i] = 2, so diff = 6 - 2 = 4
# 4 is in seen, at index 2
# Return [2, 3]

