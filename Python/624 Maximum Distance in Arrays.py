class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """

        # need to find the largest distance
        # Difference = Lagest last item - Smallest first item
        # First item array[0]
        # Last item array[-1]
        
        # Need to create first and last item lists 
        first_items =[]
        last_items = []
        
        # Loop through the given nested arrays with their indices 
        # We need the list index as well to check if later the numbers are from the same list 
        for idx, array in enumerate(arrays):
            if array: # this checks if its empty 
                first_items.append((array[0], idx)) # appending the lowest numbers and their list index into a list 
                last_items.append((array[-1], idx))
        
        # Now we need to sort the numbers by their values
        first_items.sort(key=lambda x: x[0]) # this gives us the scending order 
        last_items.sort(key=lambda x: x[0], reverse = True) # this gives us descending order because we want the numbers to start with the highest possible value 
        
        # This is a step where we check with the smallest value is in the same array as the highest value 
        if first_items[0][1] != last_items[0][1]:
            return last_items[0][0] - first_items[0][0]
        
        # If the are from the same array 
        return max(last_items[0][0] - first_items[1][0], last_items[1][0]- first_items[0][0])
                
    
    
sol = Solution()
arrays = [[1,2,3],[4,5],[1,2,3]]
result = sol.maxDistance(arrays)

print(result)
 
 
 
 