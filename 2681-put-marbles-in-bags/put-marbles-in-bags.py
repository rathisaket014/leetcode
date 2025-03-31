class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
       
        if k == 1 or n <= 2:
            return 0

        pairs = [weights[i] + weights[i + 1] for i in range(n - 1)]
        
        pairs.sort()

        minPair = sum(pairs[:k - 1])

        maxPair = sum(pairs[-(k - 1):])

        return maxPair - minPair