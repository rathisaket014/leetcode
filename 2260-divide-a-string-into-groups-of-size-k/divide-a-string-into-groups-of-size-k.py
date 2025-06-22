class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)

        ans = []
        t = ""
        j = 0

        for i in range(n):
            t += s[i]
            j += 1

            if j == k:
                ans.append(t)
                t = ""
                j = 0
        
        if len(t) != 0:
            t += fill * (k - j)
            ans.append(t)
        
        return ans