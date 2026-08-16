class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        left_bracket = ['(','{','[']
        right_bracket = [')','}',']']
        for c in s:
            if c in left_bracket:
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif len(stack) > 0:
                temp = stack.pop()
                if (temp == '(' and c == ')') or (temp == '{' and c == '}') or (temp == '[' and c == ']'):
                    continue
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False


        