#Notes
# [1,1] first index is a direcation the second is by how much
# so if its [0,1] "abc" -> "bca"
# [1,1] "abc" -> "cab" 

# so if its directio 0 we want to subtract the second index "amount" from total 
# is its directio 1 we want to add 
# [0,1] and [1,2] = amount would be -1 +2 = 1


class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """

        # Start total shift at 0 to keep track 
        move = 0 

        # Calculate the shift 
        for direction, amount in shift: 
            # if the amount is 0 then we want to subtract the movement amount
            if direction == 0: 
                move -= amount 
            # Otherwise we want to add the amount 
            else: 
                move += amount 

        # Re calculate for the length on the string 
        # We want a non negative number & remains within the range of the string 
        reshift = abs(move) % len(s)

        if move > 0: # if the shift is positive 
            #s[-reshift:] character that will be moved to the beginning of the sting 
            #s[:-reshift] remaining characters 
            s = s[-reshift:] + s[:-reshift]
        else: 
            s = s[reshift:] + s[:reshift] 
        
        return s