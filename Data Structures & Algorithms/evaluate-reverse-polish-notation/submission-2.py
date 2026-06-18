class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = ['+', '-', '*', '/']
        stack = []        
        res = 0

        for op in tokens:
            if op not in operators:
                stack.append(int(op))
            elif stack:
                op1 = stack.pop()
                op2 = stack.pop()
                op3 = 0
                if op == '+':
                    op3 = op2 + op1
                elif op == '-':
                    op3 = op2 - op1
                elif op == '*':
                    op3 = op2 * op1
                else:
                    op3 = int(op2 / op1)
                stack.append(op3)
            print(stack)
        res = stack.pop()
        return res