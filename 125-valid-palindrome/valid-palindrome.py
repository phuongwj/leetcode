class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""

        for i in range(len(s)):
            if s[i].isalnum():
                new_s += s[i]

        return new_s == new_s[::-1]