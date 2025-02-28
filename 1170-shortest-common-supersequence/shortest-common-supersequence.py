class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        p, q = len(str1), len(str2)
        df = [[""] * (q + 1) for _ in range(p + 1)]

        for i in range(p):
            for j in range(q):
                if str1[i] == str2[j]:
                    df[i + 1][j + 1] = df[i][j] + str1[i]
                else:
                    df[i + 1][j + 1] = max(df[i][j + 1], df[i + 1][j], key = len)
        

        lcs = df[-1][-1]

        ans, i, j = [], 0, 0

        for ch in lcs:
            while str1[i] != ch:
                ans.append(str1[i])
                i += 1
            while str2[j] != ch:
                ans.append(str2[j])
                j += 1
            ans.append(ch)
            i += 1
            j += 1

        ans.extend(str1[i:])
        ans.extend(str2[j:])

        return "".join(ans)
