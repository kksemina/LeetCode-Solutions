"""Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle."""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initiate current max and glibal amz as the firt element of the array
        current_max = global_max = nums[0]
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Calculate current_max as the maximum value between the current element and the sum of the current element and current_max.
            current_max = max(nums[i], current_max + nums[i])
            # Update global_max as the maximum value between global_max and current_max.
            global_max = max(global_max, current_max)
        return global_max
            
            