class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        
        l = r = root
        
        lh = rh = 0
        
        while l:
            lh += 1
            l = l.left
        
        while r:
            rh += 1
            r = r.right
        
        if lh == rh:
            return 2 ** lh - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)