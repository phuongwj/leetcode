class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        count = {}

        for num in arr:
            count[num] = count.get(num, 1) + 1

        occur = set()

        for num in count.values():
            if num not in occur:
                occur.add(num)
            else:
                return False

        return True