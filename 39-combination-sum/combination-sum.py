class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        n = len(candidates)
        allSubsets = []

        def findCombination(currSubset, curr, currSum):
            if currSum == target:
                allSubsets.append(currSubset.copy())
                return

            if curr == n or currSum > target:
                return

            # choose candidates branch
            currSubset.append(candidates[curr])
            findCombination(currSubset, curr, currSum + candidates[curr])

            # dont choose candidates[curr] branch
            currSubset.pop()
            findCombination(currSubset, curr + 1, currSum)
            
        # initialization
        findCombination([], 0, 0)
        
        return allSubsets