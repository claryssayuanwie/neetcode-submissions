class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'{':'}', '[' : ']', '(':')'}
        stack = [] # only opening brackets go in stack
        for char in s:
            if char in pairs:
                stack.append(char)
                # if we see a matching closing bracket, pop
            else:
                if not stack: # empty stack
                    return False
                last = stack.pop()
                if pairs[last] != char:
                    return False
        return not stack # stack must be empty when we are done. otherwise, smth is unclosed


            


