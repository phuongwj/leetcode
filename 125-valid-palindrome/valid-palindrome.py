class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ''
        for i in range(len(s)):
            lower = s[i].lower()
            if lower.isalnum():
                ns += lower

        rs = ns[::-1]

        return rs == ns