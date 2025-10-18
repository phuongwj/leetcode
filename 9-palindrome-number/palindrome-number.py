class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        xCopy = x
        reverse = 0

        while xCopy > 0:
            digit = xCopy % 10
            xCopy = xCopy // 10
            reverse = digit + (reverse * 10)

        return reverse == x