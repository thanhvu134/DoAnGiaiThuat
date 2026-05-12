class Solution:
    def isIsomorphic(self, s, t):
        m1, m2 = {}, {}
        
        for a, b in zip(s, t):
            if m1.get(a, b) != b or m2.get(b, a) != a:
                return False
            m1[a] = b
            m2[b] = a
        
        return True