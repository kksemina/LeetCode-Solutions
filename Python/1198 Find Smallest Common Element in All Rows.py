class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """

        # Crete a dictionary to store values 
        hashTable = collections.defaultdict(int)
        for sublist in mat: 
            for i in sublist: 
                hashTable[i] += 1

        # Filter the hashTable using dictionary comprehension
        # Check if the value is in each sublist
        hashTable = {key: value for key, value in hashTable.items() 
                        if all(key in sublist for sublist in mat)}

        #print(hashTable)

        # return the smallest number 
        if not hashTable:  # Check if the hashTable is empty
            return -1
        else:
            return min(hashTable.keys())


            


                
                
        
    



