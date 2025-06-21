class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        frq = Counter(word).values()

        res = inf

        for i in frq:
            curr = 0
            for j in frq:
                curr += j if j < i else max(0, j - (i + k))
            res = min(res, curr)
        
        return res