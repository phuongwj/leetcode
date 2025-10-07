class Solution:
    def isHappy(self, n: int) -> bool:
        aSet = set()

        while n != 1:
            if n in aSet:
                return False
            aSet.add(n)

            result = 0
            while n:
                digit = n % 10
                result += (digit ** 2)
                n = n // 10
            
            n = result

        return True