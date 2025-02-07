class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        diff = 0
        freq, colors = {}, {}
        res = []

        for i, j in queries:
            freq[j] = freq.get(j, 0) + 1
            if freq[j] == 1:
                diff += 1
            if i in colors:
                freq[colors[i]] -= 1
                if freq[colors[i]] == 0:
                    diff -= 1
            colors[i] = j
            res.append(diff)
        
        return res