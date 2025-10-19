class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        storage = {}

        frequencies = 0
        major = 0

        for i in range(len(nums)):
            if nums[i] in storage:
                storage[nums[i]] += 1
            else:
                storage[nums[i]] = 1

            if storage[nums[i]] > frequencies:
                frequencies = storage[nums[i]]
                major = nums[i]

        return major