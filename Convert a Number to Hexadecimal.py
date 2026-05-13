class Solution:
    def toHex(self, num):
        if num == 0:
            return "0"
        
        if num < 0:
            num += 2 ** 32
        
        hexs = "0123456789abcdef"
        res = ""
        
        while num:
            res = hexs[num % 16] + res
            num //= 16
        
        return res