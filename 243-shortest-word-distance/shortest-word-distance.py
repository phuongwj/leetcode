class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        n = len(wordsDict)

        pt1 = -1
        pt2 = -1
        currMin = n+1
        newMin = n+1

        # problem: need to figure out what to initialize currMin to?

        # ["a", "c", "b", "b", "a", "c", "b"]
        # pt1 = 0

        for i in range(n):

            if wordsDict[i] == word1:
                pt1 = i

            if pt1 >= 0 and pt2 >= 0:
                newMin = abs(pt2 - pt1)
            if newMin < currMin:
                currMin = newMin
            
            if wordsDict[i] == word2:
                pt2 = i

            if pt1 >= 0 and pt2 >= 0:
                newMin = abs(pt2 - pt1)
            if newMin < currMin:
                currMin = newMin

        return currMin

            
            
