class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ne_len = len(needle)

        for i in range(len(haystack)):
            count = i + ne_len
            check = haystack[i:count]

            if check == needle:
                return i

        return -1