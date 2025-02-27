class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        idx = {num : i for i, num in enumerate(arr)}

        df = defaultdict(lambda: 2)
        maxLen = 0
        n = len(arr)

        for i in range(n):
            for j in range(i):
                prev = arr[i] - arr[j]
                if prev in idx and idx[prev] < j:
                    df[(j, i)] = df[(idx[prev], j)] + 1
                    maxLen = max(maxLen, df[(j, i)])
        
        return maxLen if maxLen > 2 else 0