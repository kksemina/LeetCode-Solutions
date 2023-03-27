class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = [] #creating a stack or python list 
        closeToOpen = {")":"(", "]":"[", "}":"{"} #creating a hash 

        for c in s: # for all the items in the string
            if c in closeToOpen: # is the closign bracket in hash keys
                if stack and stack[-1] == closeToOpen[c]: # is the opening string equals to the appended bracket
                    stack.pop() # take out the opening sting because it matched
                else: 
                    return False # otherwise return false because there is no opening bracket
            else: 
                stack.append(c) # Append the opening bracket
        return True if not stack else False
        