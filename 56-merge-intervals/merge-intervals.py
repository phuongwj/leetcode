class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # given: [a, b], [c, d]
        # overlap occurs when (a <= d) and (c <= b)
        # sort by starting interval

        intervals.sort(key=lambda x: x[0])
        merged = []

        merged = [intervals[0]]

        for c, d in intervals[1:]:
            a = merged[-1][0]
            b = merged[-1][1]

            # overlap
            if (a <= d) and (c <= b):
                # only need to change the upper bound, the lower bound stays the same
                merged[-1][1] = max(b, d)
            else:
                merged.append([c, d])

        return merged