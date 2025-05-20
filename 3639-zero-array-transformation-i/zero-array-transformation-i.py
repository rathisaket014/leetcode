class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        m = len(queries)

        frq = [0] * (n + 1)

        for l, r in queries:
            frq[l] += 1
            frq[r + 1] -= 1
        
        cnt = 0

        for i, j in enumerate(nums):
            cnt += frq[i]
            if j > cnt:
                return False
        
        return True