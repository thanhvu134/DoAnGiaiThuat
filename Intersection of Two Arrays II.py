class Solution:
    def intersect(self, nums1, nums2):
        d = {}
        res = []
        
        for n in nums1:
            d[n] = d.get(n, 0) + 1
        
        for n in nums2:
            if n in d and d[n] > 0:
                res.append(n)
                d[n] -= 1
        
        return res