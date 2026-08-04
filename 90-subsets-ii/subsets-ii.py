class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        allSubsets = []

        def findSubsets(currSubset: List[int], curr: int):
            if curr == len(nums):
                copy = currSubset.copy()
                allSubsets.append(copy)
                return

            currSubset.append(nums[curr])
            findSubsets(currSubset, curr + 1)

            currSubset.pop()

            while curr + 1 < len(nums) and nums[curr] == nums[curr + 1]:
                curr += 1

            findSubsets(currSubset, curr + 1)

        findSubsets([], 0)
        return allSubsets