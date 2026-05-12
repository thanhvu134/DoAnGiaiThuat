class Solution:
    def guessNumber(self, n):
        left = 1
        right = n
        
        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res == 1:
                left = mid + 1
            else:
                right = mid - 1