class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # observation from recursive tree: the amount of ( and ) == n
        # have 2 variables, open and close to keep track of 
        # how many ( and ) we already have, pass them down 
        # to the recursive function as well. we would 
        # complete a combination when both open and close == n

        allCombinations = []
        def generate(open, close, combination):
            # base case
            if (open == n) and (close == n):
                allCombinations.append(combination)
                return

            # 1. open parenthesis
            if open != n:
                generate(open + 1, close, combination + "(")

            # 2. close parenthesis, only allow when there are
            # open parenthesis
            if close < open:
                generate(open, close + 1, combination + ")")

            return

        generate(0, 0, "")
    
        return allCombinations