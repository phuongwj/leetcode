# Time Complexity:
# O(n) - where n is the length of the input string 's' and 't'
# - First loop: O(n) to iterate over string 's' and increment characters inside the alphabet
# - Second loop: O(n) to iterate over string 't' and decrement characters inside the alphabet
# Space Complexity:
# O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet = [0] * 26

        for i in range(len(s)):
            alphabet[ord(s[i]) - ord('a')] += 1
        
        for i in range(len(t)):
            alphabet[ord(t[i]) - ord('a')] -= 1
        
        for i in range(len(alphabet)):
            if alphabet[i] != 0: 
                return False
        
        return True