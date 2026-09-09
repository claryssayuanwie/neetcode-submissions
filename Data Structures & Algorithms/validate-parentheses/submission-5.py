class Solution:
    def isValid(self, s: str) -> bool:
        # key:val = close:open
        hashmap = {')':'(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if c not in hashmap:
                # c is an opening bracket and should be added to stack
                stack.append(c)
            else:
                if not stack: # empty stack
                    return False
                else:
                    # if thing we pop is not corresponding with c
                    popped = stack.pop()
                    if popped != hashmap[c]:
                        return False
        return not stack # stack is empty (return not stack should be true)
