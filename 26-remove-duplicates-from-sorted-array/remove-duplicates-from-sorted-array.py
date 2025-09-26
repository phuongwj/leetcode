class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0 or n == 1:
            return n

        else:
            curr = 0
            nxt = curr+1
            while curr != len(nums):

                if nums[curr] == nums[nxt]:
                    nums.pop(nxt)
                    
                    if len(nums) == 1:
                        break
                        
                elif nums[curr] != nums[nxt]:
                    curr += 1
                    nxt = curr+1

                if nxt > len(nums)-1:
                    break

        return len(nums)