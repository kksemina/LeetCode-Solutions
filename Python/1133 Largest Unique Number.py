class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Go through all the numbers and delete any that appear more than once 
        hash = Counter(nums)
        new = []

        for num, i in hash.items(): 
            if i == 1:
                new.append(num)
        
        new = sorted(new)

        # If the list is empty return -1
        if len(new) == 0: 
            return -1
        else: 
            return new[-1]