class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        val = 0
        pwr = 1
        res = 0

        for ch in reversed(s):
            if ch == '0':
                res += 1
            else:
                if pwr <= k and val + pwr <= k:
                    val += pwr
                    res += 1

            pwr <<= 1
            if pwr > k:
                break

        res += s[:len(s) - res].count('0')
        return res      