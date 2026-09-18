class Solution:
    def maximum69Number (self, num: int) -> int:

        strNum = str(num)
        n = len(strNum)

        for i in range(n):
            if strNum[i] == '6':
                strNum = strNum[:i] + "9" + strNum[i+1:]
                return int(strNum)

        return int(strNum)