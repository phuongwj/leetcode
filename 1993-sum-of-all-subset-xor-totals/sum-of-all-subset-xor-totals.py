class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        n = len(nums)
        total = 0

        for mask in range(1, 1 << n):
            xor = 0

            for i in range(n):
                if mask & (1 << i):
                    xor ^= nums[i]

            total += xor

        return total