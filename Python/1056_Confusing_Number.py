"""A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.

We can rotate digits of a number by 180 degrees to form new digits.

When 0, 1, 6, 8, and 9 are rotated 180 degrees, they become 0, 1, 9, 8, and 6 respectively.
When 2, 3, 4, 5, and 7 are rotated 180 degrees, they become invalid.
Note that after rotating a number, we can ignore leading zeros.

For example, after rotating 8000, we have 0008 which is considered as just 8.
Given an integer n, return true if it is a confusing number, or false otherwise.

 

Example 1:


Input: n = 6
Output: true
Explanation: We get 9 after rotating 6, 9 is a valid number, and 9 != 6.
Example 2:


Input: n = 89
Output: true
Explanation: We get 68 after rotating 89, 68 is a valid number and 68 != 89.
Example 3:


Input: n = 11
Output: false
Explanation: We get 11 after rotating 11, 11 is a valid number but the value remains the same, thus 11 is not a confusing number
 

Constraints:

0 <= n <= 109
"""

# Notes 
#Set a list of all the valid digits {0,1,6,8,9}
#Dictionary or hash map {0:0,1:1,6:9,8:8,9:6}
#When we do the rotation the order of numbers change so reverse the numbers
#Check if the number is confusing or not

#Solution

class Solution(object):
    def confusingNumber(self, n):
        """
        :type n: int
        :rtype: bool
        """
  
        # Use 'invertMap' to invert each valid digit.
        invert_map = {"0":"0", "1":"1", "8":"8", "6":"9", "9":"6"}
        rotated_number = []
        
        for number in str(n):
            if number not in invert_map:
                return False 
            #If the number in in the map append it to the end of rotated number
            rotated_number.append(invert_map[number])
        #Join elements into same string
        rotated_number = "".join(rotated_number)

        #Check if the number is confusing or not 
        return int(rotated_number[::-1]) != n

