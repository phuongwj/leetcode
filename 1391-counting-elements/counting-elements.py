class Solution:
    def countElements(self, arr: List[int]) -> int:
        """
        Constraints is small enough for the O(n^2) brute-force solution to pass
        """

        counter = 0
        n = len(arr)

        for i in range(n):
            extra = arr[i] + 1
            if extra in arr:
                counter += 1

        return counter