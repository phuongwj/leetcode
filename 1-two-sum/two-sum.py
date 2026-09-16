class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        storage = {}
        n = len(nums)

        arr = []

        for i in range(n):
            complement = target - nums[i]

            if complement in storage.keys():
                arr.append(i)
                arr.append(storage[complement])
            else:
                storage[nums[i]] = i

        return arr    