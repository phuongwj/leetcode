class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}

        for i in range(len(nums)):
            if nums[i] not in nums_map:
                nums_map[nums[i]] = 1
            else:
                return True

        return False