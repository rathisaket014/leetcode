class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        cnt = Counter(n for arr in grid for n in arr)

        for i in cnt:
            if (grid[0][0] - i) % x:
                return -1
        
        arr, prev, curr, mincnt, maxcnt = [], 0, 0, min(cnt), max(cnt)

        for n in range(mincnt, maxcnt + 1, x):
            arr.append(prev + curr)
            prev, curr = arr[-1], curr + cnt[n]
        
        ans, curr, nxt = inf, 0, 0

        for n in range(maxcnt, mincnt - 1, -x):
            ans = min(ans, arr.pop() + curr + nxt)
            curr, nxt = curr + cnt[n], curr + nxt
        
        return ans