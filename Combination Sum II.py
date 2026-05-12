class Solution:
    def combinationSum2(self, c, t):
        c.sort()
        res = []
        def dfs(start, path, s):
            if s == t:
                res.append(path)
                return
            for i in range(start, len(c)):
                if i > start and c[i] == c[i-1]:
                    continue
                if s + c[i] > t:
                    break
                dfs(i+1, path+[c[i]], s+c[i])
        dfs(0, [], 0)
        return res