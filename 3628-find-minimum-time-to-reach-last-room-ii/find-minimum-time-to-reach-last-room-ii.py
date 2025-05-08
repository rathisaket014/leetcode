class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])

        INF = float('inf')
        dp = [[INF] * m for _ in range(n)]
        heap = [(0, 0, 0)]
        moveTime[0][0] = 0

        ways = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while heap:
            time, r, c = heapq.heappop(heap)
            if time >= dp[r][c]:
                continue
            if r == n - 1 and c == m - 1:
                return time
            dp[r][c] = time
            for x, y in ways:
                nxtR = r + x
                nxtC = c + y

                if 0 <= nxtR < n and 0 <= nxtC < m and dp[nxtR][nxtC] == INF:
                    cost = (r + c) % 2 + 1
                    count = max(moveTime[nxtR][nxtC], time)
                    nxtTime = count + cost
                    heapq.heappush(heap, (nxtTime, nxtR, nxtC))
        return -1