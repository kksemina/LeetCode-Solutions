class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values = {} # create dictionary 
        for i in range(len(nums)): # loop through index and numbers 
            left_over = target - nums[i] # find difference between number and target
            if left_over in values: #check if the value is in dict
                return [values[left_over], i] # return the index of the difference and number
            else:
                values[nums[i]] = i # add the number and index into dict
