class Solution:
    def longestPalindrome(self, s):
        d = {}
        ans = 0
        odd = False
        
        for c in s:
            d[c] = d.get(c, 0) + 1
        
        for v in d.values():
            ans += (v // 2) * 2
            if v % 2 == 1:
                odd = True
        
        return ans + 1 if odd else ans