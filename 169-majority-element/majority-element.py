class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        storage = {}

        for i in range(len(nums)):
            if nums[i] in storage:
                storage[nums[i]] += 1
            else:
                storage[nums[i]] = 1

        maxValue = max(storage.values())

        for key in storage.keys():
            if storage[key] == maxValue:
                return key

        