class Solution:
    def combinationSum(self, c, t):
        res = []
        def dfs(i, path, s):
            if s == t:
                res.append(path)
                return
            if s > t or i == len(c):
                return
            dfs(i, path + [c[i]], s + c[i])
            dfs(i + 1, path, s)
        dfs(0, [], 0)
        return res