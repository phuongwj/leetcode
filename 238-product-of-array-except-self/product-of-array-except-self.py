class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        for each number, find product of everything except itself
        observation: for each number, we take everything before and
        after it, multiply together.
        => Prefix product except self
        => Suffix product except self
        """

        n = len(nums)

        preProd = [1] * n
        suffProd = [1] * n

        for i in range(1, n):
            preProd[i] = preProd[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            suffProd[i] = suffProd[i+1] * nums[i+1]

        output = [1] * n
        for i in range(n):
            output[i] = preProd[i] * suffProd[i]
            
        return output