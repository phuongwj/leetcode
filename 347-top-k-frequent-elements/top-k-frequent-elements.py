class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in range(len(nums)):
            if nums[i] not in freq.keys():
                freq[nums[i]] = freq.get(nums[i], 1)
            else:
                freq[nums[i]] += 1
        
        sorted_list = sorted(list(freq.values()), reverse = True)
        return_list = []

        for key in freq.keys():
            if freq[key] >= sorted_list[k-1]:
                return_list.append(key)

        return return_list
