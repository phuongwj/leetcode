class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sorts array first
        candidates.sort()
        res = []

        def backtrack(i, curr, total):

            if total == target:
                res.append(curr.copy())
                return

            if i == len(candidates) or total > target:
                return

            # branch 1: take
            curr.append(candidates[i])
            backtrack(i + 1, curr, total + candidates[i])
            curr.pop()

            # branch 2: dont take
            j = i + 1

            # Skip identical numbers
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1

            backtrack(j, curr, total)

        backtrack(0, [], 0)

        return res