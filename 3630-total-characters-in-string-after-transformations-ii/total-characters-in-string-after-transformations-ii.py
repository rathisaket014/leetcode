MOD = 10**9 + 7

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        mat = [[0] * 26 for _ in range(26)]

        for i in range(26):
            for j in range(nums[i]):
                mat[i][(i + j + 1) % 26] += 1

        def mul(a, b):
            res = [[0] * 26 for _ in range(26)]
            for x in range(26):
                for y in range(26):
                    if a[x][y] == 0:
                        continue
                    for z in range(26):
                        res[x][z] = (res[x][z] + a[x][y] * b[y][z]) % MOD
            return res

        def expo(matrix, power):
            result = [[int(i == j) for j in range(26)] for i in range(26)]
            while power:
                if power % 2:
                    result = mul(result, matrix)
                matrix = mul(matrix, matrix)
                power //= 2
            return result

        final = expo(mat, t)

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        total = 0
        for i in range(26):
            for j in range(26):
                total = (total + freq[i] * final[i][j]) % MOD

        return total
