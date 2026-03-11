class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}

        for i in range(len(nums)):
            num = nums[i]

            subtract = target - num
            if subtract not in mapp.keys():
                mapp[num] = i
            else:
                return [mapp[subtract], i]

        return []