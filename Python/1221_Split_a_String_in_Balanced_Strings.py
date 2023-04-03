class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        # creating two counts
        # count will keep track of balanced substrings
        # balance will keep track of the difference between L and R numbers
        count = 0
        balance = 0
        
        # for each character in string
        for char in s:
            # If its L it will add one
            if char == 'L':
                balance += 1
            # otherwise it will take away 1
            else:
                balance -= 1
            # if balance is 0 than we know we have at least one pair of characters
            if balance == 0:
                count += 1
        
        return count
        
    
