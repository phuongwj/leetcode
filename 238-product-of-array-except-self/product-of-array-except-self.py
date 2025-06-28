class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [0] * len(nums)
        zero_count = nums.count(0)

        if zero_count > 1:
            return product 
        
        total_product = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                total_product *= nums[i]
        
        if zero_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    product[i] = total_product
                else:
                    product[i] = 0
        else:
            for i in range(len(nums)):
                product[i] = total_product // nums[i]

        return product