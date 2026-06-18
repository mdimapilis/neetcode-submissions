class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for c in s:
            if c in bracket:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                elif c != bracket[stack.pop()]:
                    return False
                
        return len(stack) == 0