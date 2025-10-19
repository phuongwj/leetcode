class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)

        ptr = 0

        for i in range(n):
            s += s[ptr]
            s = s[:ptr] + s[ptr + 1:]

            if s == goal:
                return True

        return False