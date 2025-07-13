class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        print(nums)

        if not nums:
            return 0
        elif len(nums) == 1:
            return 1

        curr = nums[0]
        ans = 0
        longest = 1
        for i in range(1, len(nums)):
            nxt = nums[i]
            if nxt - curr == 1:
                longest += 1
            elif nxt - curr == 0:
                pass
            else:
                ans = max(ans, longest)
                longest = 1
            curr = nxt

        ans = max(ans, longest)

        return ans