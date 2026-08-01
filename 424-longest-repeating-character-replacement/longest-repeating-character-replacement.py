class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Find the longest substring containing the same letters
        after replacing the string k times. 

        Sliding Window pattern. Have a left and a right, left is 
        to anchor the start of the window, right is to keep the 
        window moving forward to check for window's validness. At 
        each point, we will count whether we will need to change 
        the string, we keep doing that while also keeping track 
        of the longest substring. At any current window, if it has 
        become invalid, we will move left forward and check for the 
        other windows. Why we're moving left and no need to move 
        right back is because we're always looking for a bigger 
        substring than what we already have, and resetting right 
        is redundant, as we will have to keep re-checking for the 
        length that is less than what we already have.
        """

        n = len(s)

        if n == 1:
            return 1
        
        max_freq = 0 # how many times we've change letter
        max_len = 0 # what we're returning
        count = {}
        left = 0
        right = 0

        while right < n:
            right_char = s[right]
            count[right_char] = count.get(right_char, 0) + 1

            max_freq = max(max_freq, count[right_char])

            window_len = right - left + 1

            if window_len - max_freq > k:
                left_char = s[left]
                count[left_char] -= 1
                left += 1

            # re-calculate window length cause left shrinked
            window_len = right - left + 1

            max_len = max(max_len, window_len)

            right += 1

        return max_len