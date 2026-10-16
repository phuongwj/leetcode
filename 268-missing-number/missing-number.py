class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        maxLen = n + 1

        expectedSum = 0
        for i in range(maxLen):
            expectedSum += i

        actualSum = 0
        for num in nums:
            actualSum += num
            
        return expectedSum - actualSum