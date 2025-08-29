class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] not in hashmap.keys():
                hashmap[nums[i]] = hashmap.get(nums[i], i)
            else:
                length = abs(hashmap[nums[i]] - i)
                if length <= k:
                    return True
                hashmap[nums[i]] = i

        return False