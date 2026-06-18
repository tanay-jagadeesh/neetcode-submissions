class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['*', '+', '-', '/']

        for op in tokens: 
            if op not in operands:
                stack.append(op)
            elif op in operands and stack:
                b = int(stack.pop())
                a = int(stack.pop())
                if op == '*':
                    stack.append(a * b)
                elif op == '+':
                    stack.append(a + b)
                elif op == '-':
                    stack.append(a - b)
                else:
                    stack.append(int(a/b))
        return int(stack[0])