class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # First lets sort the values in order of biggest to smallest number
        sorted_nums = sorted(nums, reverse=True)
        # Creating a dictionary for our outputs
        smaller_count = {}
        # Looping over the range of length number in sorted numbers list -1
        for i in range(len(sorted_nums)-1):
            curr_num = sorted_nums[i]
            next_num = sorted_nums[i+1]
            # We want to check if our current number is bigger than the next one 
            if next_num < curr_num:
                # If it is smaller, it calculates the number of remaining values in the list 
                # (because we know all the other values have to be smaller to)
                remaining_values = len(sorted_nums) - (i+1)
                smaller_count[curr_num] = remaining_values
        # Set the last value to 0 
        smaller_count[sorted_nums[-1]] = 0

        # We need to loop through the dictionary and get the right number for each value in the original list
        output = []
        for num in nums: 
            output.append(smaller_count[num])

        return output

# Create an instance of the Solution class
solution = Solution()
# List of numbers
nums = [8,1,2,2,3]
# Call the function 
result = solution.smallerNumbersThanCurrent(nums)
print(result)


