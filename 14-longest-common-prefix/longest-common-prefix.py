class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # the whole array needs to have the same prefix string

        n = len(strs[0])
        first = strs[0]
        prefix = ""

        if len(strs) == 1:
            return strs[0]

        for i in range(1, n+1):
            prefix = first[:i]

            for string in strs:
                if not string.startswith(prefix):
                    return prefix[:-1]

        return prefix