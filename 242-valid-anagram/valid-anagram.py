class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet = 26 * [0]

        for i in range(len(s)):
            index = ord('z') - ord(s[i])
            alphabet[index] += 1

        for i in range(len(t)):
            index = ord('z') - ord(t[i])
            alphabet[index] -= 1

        for a in alphabet:
            if a > 0 or a < 0:
                return False
        
        return True