class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start = 0 
        end = len(nums)-1

        while start <= end: 
            mid = (start + end) // 2
            num = nums[mid]
            if target == num:
                return mid
            elif target > num:
                start = mid +1
            elif target < num:
                end = mid -1
        return -1
        
        
# Create an instance of the Solution class
solution = Solution()
# List of numbers
nums = [-1,0,3,5,9,12]
target = 9
# Call the function 
result = solution.search(nums, target)
print(result)