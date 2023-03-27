class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        # Sorting the values first so we can get the largest amount of coin piles easier 
        sorted_piles = sorted(piles)
        # Get the last index in the list
        end_index = len(piles) -1
        # starting index
        our_value = 0 
        for i in range(len(piles)//3):
            # Our value is the largest pile -1 (one smaller)
            # so we want to go to the end_index and 
            # Its i*2 because we are looking at two items 
            our_value += sorted_piles[end_index-(i*2)-1]

        return our_value