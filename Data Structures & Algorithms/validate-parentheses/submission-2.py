class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}  # closed -> open

        for i in s:
            if i in pairs:
                if stack and stack[-1] == pairs[i]:  # does top of stack match?
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)                   # it's an opening bracket

        return len(stack) == 0
