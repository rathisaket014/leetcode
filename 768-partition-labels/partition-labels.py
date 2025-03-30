class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        Idx = {}
        for i, c in enumerate(s):
            Idx[c] = i
        
        res = []
        st, en = 0, 0

        for i, c in enumerate(s):
            st += 1
            if Idx[c] > en:
                en = Idx[c]
            if i == en:
                res.append(st)
                st = 0
        
        return res