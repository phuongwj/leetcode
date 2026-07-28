class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if not n:
            return 0
        elif n == 1:
            return 1

        """
        Sliding window pattern. Have a left and a right, left is to anchor the start of a  window, right is the pointer to keep adding to the window. If we've reached a right value that's already in the window, and add it to the window, window becomes invalid. And so, we need to keep shrinking the window (which also keeps as much of the window as possible), so window can become valid with the new right. Use a set to keep track of unique characters.
        """

        """
        Set is storing s[left:right]
        right is the character we're trying to add
        """
        
        chars = set()
        left = 0
        right = 0
        longest = 0

        while right < n:

            if s[right] not in chars:
                chars.add(s[right])
                right += 1
            else:
                while s[right] in chars:
                    chars.remove(s[left])
                    left += 1

            if len(chars) > longest:
                longest = len(chars)

        return longest