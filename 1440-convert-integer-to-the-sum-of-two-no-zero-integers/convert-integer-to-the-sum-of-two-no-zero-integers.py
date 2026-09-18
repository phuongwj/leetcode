class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:

        retList = []

        for i in range(1, n):
            num1 = n - i

            if '0' not in str(num1) and '0' not in str(i):
                retList.append(num1)
                retList.append(i)
                return retList

        return retList