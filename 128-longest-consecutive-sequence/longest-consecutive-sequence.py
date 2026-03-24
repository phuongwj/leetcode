class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        if not nums:
            return 0        
        
        longest = 1
        output = []
        for i in range(len(nums)):
            nxt = i + 1
            if nxt == len(nums):
                output.append(longest)
                return max(output)

            if nums[nxt] - nums[i] == 1:
                longest += 1
            elif nums[nxt] - nums[i] > 1:
                output.append(longest)
                longest = 1
            else:
                pass

        return max(output)