class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        """
        backtracking, recursion.
        we have two choices for each number.
        """
        
        allSubsets = []

        def findSubsets(currSubset, curr):
            # we've reached the last element if index is out of bounds
            if curr == len(nums):
                copy = currSubset.copy()
                allSubsets.append(copy)
                return

            # include branch.
            currSubset.append(nums[curr])
            findSubsets(currSubset, curr + 1)

            # exclude branch. note: if you exclude it, you must pop the 
            # most recent one so you can add the one after it.
            currSubset.pop()
            findSubsets(currSubset, curr + 1)
            

        # gives first index
        findSubsets([], 0)
        return allSubsets