class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        frq = [0] * 26

        for ch in s:
            frq[ord(ch) - ord('a')] += 1
        
        for _ in range(t):
            alpha = frq[25]
            f0 = frq[0]
            for i in range(25, 1, -1):
                frq[i] = frq[i - 1]
            frq[0] = alpha
            f0 += alpha
            if f0 >= mod:
                f0 -= mod
            frq[1] = f0
        
        return sum(frq) % mod