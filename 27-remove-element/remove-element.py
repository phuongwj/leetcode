class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        newlen = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[newlen] = nums[i]
                newlen += 1

        return newlen