class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        freq = [0] * 32 # 32 because the largest num is 10^7, and largest number of bits is 32
        maxCom = 0

        for can in candidates:
            for bit in range(32):
                if can & (1 << bit):
                    freq[bit] += 1
                    maxCom = max(maxCom, freq[bit])
        
        return maxCom