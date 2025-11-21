class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = []

        for i in range(len(nums)):
            squared.append(nums[i] * nums[i])
        
        squared.sort()

        return squared