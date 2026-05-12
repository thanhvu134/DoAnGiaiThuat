class Solution:
    def isValid(self, s):
        stack = []
        m = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in m.values():
                stack.append(ch)
            else:
                if not stack or stack.pop() != m[ch]:
                    return False

        return not stack