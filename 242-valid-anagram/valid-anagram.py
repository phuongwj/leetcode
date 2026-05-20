class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet = [0] * 26

        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            alphabet[idx] += 1

        for i in range(len(t)):
            idx = ord(t[i]) - ord('a')
            alphabet[idx] -= 1

        return all(x == 0 for x in alphabet)