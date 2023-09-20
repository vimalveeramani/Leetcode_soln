class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        result = ""
        for char in s:
            if char == '(':
                if count > 0:
                    result+=char
                count += 1
            elif char == ')':
                count -= 1
                if count > 0:
                    result+=char
            else:
                if count > 0:
                    result+=char
        return result
