class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)
        i = 0

        for k in s:
            if k.isdigit() and i > 0:
                i -= 1
            else:
                s[i] = k
                i += 1

        return "".join(s[:i])