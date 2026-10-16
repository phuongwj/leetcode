class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        sLen = len(s)
        aLen = len(a)
        bLen = len(b)

        beautifulI = []
        beautifulJ = []
        for i in range(sLen):
            if s[i:i+aLen] == a:
                beautifulI.append(i)
            if s[i:i+bLen] == b:
                beautifulJ.append(i)

        output = []
        if not beautifulJ:
            return output

        for i in beautifulI:
            for j in beautifulJ:
                if abs(i - j) <= k:
                    output.append(i)
                    break

        return output