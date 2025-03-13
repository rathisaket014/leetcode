class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)

        pf = [0] * (n + 1)
        curr = 0
        idx = 0

        for i, num in enumerate(nums):
            curr += pf[i]
            while idx < m and curr < num:
                left, right, val = queries[idx]
                idx += 1
                if i < left:
                    pf[left] += val
                elif i <= right:
                    curr += val
                pf[right + 1] -= val
            if curr < num:
                return -1
        
        return idx