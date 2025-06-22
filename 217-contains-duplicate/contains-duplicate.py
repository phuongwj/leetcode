class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}

        for i in range(len(nums)):
            if nums[i] not in duplicates.keys():
                duplicates[nums[i]] = duplicates.get(nums[i], 0) + 1
            else:
                return True

        return False