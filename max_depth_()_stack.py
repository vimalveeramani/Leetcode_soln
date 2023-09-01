class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        stack = []
        for i in range (len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if count < len(stack):
                    count = len(stack)
                
                stack.pop()
        return count
        
