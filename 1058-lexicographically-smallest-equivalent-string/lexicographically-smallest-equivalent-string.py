class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        def union(x, y):
            rx = find(x)
            ry = find(y)

            if rx != ry:
                if rx < ry:
                    p[ry] = rx
                else:
                    p[rx] = ry
        
        p = {chr(i) : chr(i) for i in range(ord('a'), ord('z') + 1)}

        for i, j in zip(s1, s2):
            union(i, j)
        res = []

        for c in baseStr:
            res.append(find(c))
        return "".join(res)