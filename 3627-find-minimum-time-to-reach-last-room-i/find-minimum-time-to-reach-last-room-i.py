from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        r = len(moveTime)
        c = len(moveTime[0])

        if r == 1 and c == 1:
            return 0
        
        vis = set()
        vis.add((0, 0))

        h = [(0, 0, 0)]
        while h:
            ways = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            time, row, col = heappop(h)

            if (row, col) == (r - 1, c - 1):
                return time
            for dx, dy in ways:
                nxtRow, nxtCol = row + dx, col + dy
                if 0 <= nxtRow < r and 0 <= nxtCol < c and (nxtRow, nxtCol) not in vis:
                    heappush(h, (max(time, moveTime[nxtRow][nxtCol]) + 1, nxtRow, nxtCol))
                    vis.add((nxtRow, nxtCol))
        return -1