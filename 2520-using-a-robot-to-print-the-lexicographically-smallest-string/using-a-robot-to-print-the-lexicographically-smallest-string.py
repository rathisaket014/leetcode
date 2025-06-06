class Solution:
    def robotWithString(self, s: str) -> str:
        min_ch = min(s)
        ch_count = s.count(min_ch)
        res = ""

        stk = []
        en = len(s) - 1

        for i, ch in enumerate(s):
            if ch == min_ch:
                res += ch
                ch_count -= 1
                if ch_count == 0:
                    if i >= en:
                        break
                    min_ch = min(s[i + 1 :])
                    ch_count = s[i + 1:].count(min_ch)
                    while stk and stk[-1] <= min_ch:
                        res += stk.pop()
            else:
                stk.append(ch)
        
        return res + "".join(stk[::-1])