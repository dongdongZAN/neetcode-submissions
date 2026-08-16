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

        # stack = []
        # closeToOpen = {")":"(", "]":"[", "}":"{"}

        # for c in s:
        #     if c in closeToOpen:
        #         if stack and stack[-1] == closeToOpen[c]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(c)
        
        # return True if not stack else False


        