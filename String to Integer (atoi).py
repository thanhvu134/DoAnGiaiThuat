class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)
        sign = 1
        res = 0
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        while i < n and s[i] == ' ':
            i += 1

        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        while i < n and s[i].isdigit():
            res = res * 10 + (ord(s[i]) - ord('0'))
            i += 1

        res *= sign
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
        return res
