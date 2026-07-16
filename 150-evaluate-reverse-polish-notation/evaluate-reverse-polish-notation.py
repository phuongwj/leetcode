class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == "+":
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif tokens[i] == "*":
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(int(float(second) / first))
            else:
                stack.append(int(tokens[i]))
        return stack[0]