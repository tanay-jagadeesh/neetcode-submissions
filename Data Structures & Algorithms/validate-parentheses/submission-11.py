class Solution:
    def isValid(self, s: str) -> bool:
        matches = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s: 
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif stack and stack[-1] == matches[c]:
                stack.pop()
            else:
                return False
        return stack == []
        