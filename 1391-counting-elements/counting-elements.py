class Solution:
    def countElements(self, arr: List[int]) -> int:

        counter = 0
        n = len(arr)

        for i in range(n):
            extra = arr[i] + 1
            if extra in arr:
                counter += 1

        return counter