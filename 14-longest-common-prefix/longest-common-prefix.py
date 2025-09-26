class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        shortestStr = min(strs, key=len)
        

        # Start with the shortest string
        # For every single prefix of the shortest string, we
        # check if the other strings start with the prefix
        # if we found a prefix that doesn't match for any string, 
        # then the previous prefix is our answer 

        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 0:
            return ""

        prefix = ""

        for i in range(1, len(shortestStr) + 1):
            prefix = shortestStr[:i]

            for string in strs:
                if not string.startswith(prefix):
                    return shortestStr[:i-1]

        return prefix