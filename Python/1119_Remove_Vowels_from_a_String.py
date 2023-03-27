class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        Result = ""
        vowels ={"a","e","i","o","u"}
        for i in s:
            if i not in vowels:
                Result+=i
        return Result


# Create an instance of the Solution class
solution = Solution()
#string
s = "aeioub"
#call function 
result = solution.removeVowels(s)
print(result)