class Solution:
    def countElements(self, arr: List[int]) -> int:
        """
        Constraints are small enough for the O(n^2) brute-force solution to pass

        Can use hash set to store all numbers in arr, which gives us O(1) lookup.
        Time complexity: O(n) and Space Complexity O(n)
        """

        storage = set()
        n = len(arr)

        for i in range(n):
            if arr[i] not in storage:
                storage.add(arr[i])

        counter = 0

        for i in range(n):
            extra = arr[i] + 1
            if extra in storage:
                counter += 1

        return counter