class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+','-','*','/']
        res = 0
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if token == '+':
                    res = a + b
                    stack.append(res)
                if token == '-':
                    res = b - a
                    stack.append(res)
                if token == '*':
                    res = a * b
                    stack.append(res)
                if token == '/':
                    res = b / a
                    stack.append(res)
        return int(stack.pop())


        