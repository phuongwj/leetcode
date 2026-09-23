class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        count = 0

        def isBeautiful(subset: List[int]):
            for i in range(len(subset)):
                for j in range(i + 1, len(subset)):
                    if abs(subset[i] - subset[j]) == k:
                        return False
            
            return True

        def generate(i, subset):
            # to be able to modify count which was declared outside the function
            nonlocal count 

            # only check once we finished generating all subsets
            if i == len(nums):
                if subset and isBeautiful(subset):
                    count += 1
                return

            subset.append(nums[i])
            generate(i+1, subset)
           
            subset.pop()
            generate(i+1, subset)

        generate(0, [])

        return count