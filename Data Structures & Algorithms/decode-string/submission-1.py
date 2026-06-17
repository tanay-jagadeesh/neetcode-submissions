class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * substr)
        return "".join(stack)

    """
    e.g. s = "2[a3[b]]c"

    looking at input we see 3 * b so 3 b's and 1 a repeat twice and then c

    final output: "abbbabbbc"

    thoughts: 
    -how to detect k[string] in s

    """