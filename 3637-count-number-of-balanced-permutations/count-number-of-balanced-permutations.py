class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        cnt = Counter(int(x) for x in num)
        total = sum(int(x) for x in num)
        MOD = 10**9 + 7

        n = len(num)
        @cache
        def DFS(i, odd, even, bal):
            if odd == 0 and even == 0 and bal == 0:
                return 1
            if i < 0 or odd < 0 or even < 0 or bal < 0:
                return 0
            res = 0
            for k in range(0, cnt[i] + 1):
                res += comb(odd, k) * comb(even, cnt[i] - k) * DFS(i - 1, odd - k, even - cnt[i] + k, bal - i * k)
            return res % MOD
        
        return 0 if total % 2 else DFS(9, n - n // 2, n // 2, total // 2)