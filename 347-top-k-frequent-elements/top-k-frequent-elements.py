class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top = {}

        for i in range(len(nums)):
            num = nums[i]

            if num not in top:
                top[num] = 0
                top[num] += 1
            else:
                top[num] += 1

        return heapq.nlargest(k, top.keys(), key=top.get)