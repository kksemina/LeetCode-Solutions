"""
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

        Example 1:

        Input: nums = [1,2,3,1]
        Output: true
        Example 2:

        Input: nums = [1,2,3,4]
        Output: false
        Example 3:

        Input: nums = [1,1,1,3,3,4,3,2,4,2]
        Output: true
        

        Constraints:

        1 <= nums.length <= 105
        -109 <= nums[i] <= 109
            
    """
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
       # initiate an empty hash table 
        table = set()
        #Iterate through each element in the array nums
        for num in nums: 
            #If the current element is already in the hash set, return true (as it indicates a duplicate)
            if num in table: 
                return True 
            #Otherwise, add the element to the hash set
            table.add(num)
        #If we have iterated through the entire array without finding any duplicates, return false
        return False


