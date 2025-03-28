class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        row, col = len(grid), len(grid[0])
        res = [0] * len(queries)

        heap = [(grid[0][0], 0, 0)]
        directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]

        grid[0][0] = 0
        count = 0

        for qi, q in sorted(enumerate(queries), key = lambda x: x[1]):
            while heap and heap[0][0] < q:
                _, i, j = heappop(heap)
                count += 1
                for x, y in directions:
                    r, c = i + x, j + y
                    if r >= 0 and r < row and c >= 0 and c < col and grid[r][c]:
                        heappush(heap, (grid[r][c], r, c))
                        grid[r][c] = 0
        
            res[qi] = count

        return res 