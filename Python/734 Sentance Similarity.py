class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """

        # set variables 
        S1 = len(sentence1)
        S2 = len(sentence2)

        # crate a set for words 
        similarDict = collections.defaultdict(set)
        for a,b in similarPairs: 
            similarDict[a].add(b)
            similarDict[b].add(a)

        # First check if the sentances are the same length 
        if S1 != S2: 
            return False 

        # Check similarity 
        for i in range(S1):
            # if the A = B and check if B = A 
            if sentence1[i] != sentence2[i] and sentence2[i] not in similarDict[sentence1[i]]:
                return False 

        return True