class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []

        for i in range(len(nums)):
            if not left:
                left.append(1)
            else:
                prod = left[i-1] * nums[i-1]
                left.append(prod)

        output = []
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            calc = right * left[i]
            right = right * nums[i]
            output.append(calc)

        output.reverse()
        return output