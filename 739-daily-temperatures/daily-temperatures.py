class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Brute-force solution: For every single number, check if the very next number is
        larger than it, if not we keep on moving to the next number until we reach the end.
        Every time we move over like that, we will take the index of the larger number and
        subtract the index of the current number and append the difference into output array. 
        If we reach the end and no larger number is found, then we append 0 to output array.

        Observation: [75, 71, 72, 78]. While at 75, I had to go through 71 and 72 to find 78.
        And when I get to 71, I'm essentially going through it again even though I went through
        it already when I was at 75.
        """

        n = len(temperatures)
        output = [0] * n
        unresolved = []

        for curr in range(n):

            while unresolved and temperatures[curr] > temperatures[unresolved[-1]]:
                diff = curr - unresolved[-1]
                output[unresolved[-1]] = diff
                unresolved.pop()

            unresolved.append(curr)

        return output