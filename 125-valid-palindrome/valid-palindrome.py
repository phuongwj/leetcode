class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        s = s.lower()

        for i in range(len(s)):
            if s[i].isalnum():
                new += s[i]
            
        rev = "".join(reversed(new))

        return rev == new