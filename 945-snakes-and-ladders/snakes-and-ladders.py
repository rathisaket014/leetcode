from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        cells = [-1] * (n * n)
        idx = 0
        even_row = True
        for i in range(n - 1, -1, -1):
            row = range(n) if even_row else range(n - 1, -1, -1)
            for j in row:
                if board[i][j] != -1:
                    cells[idx] = board[i][j] - 1
                idx += 1
            even_row = not even_row

        # BFS
        visited = [-1] * (n * n)
        q = deque([0])
        visited[0] = 0

        while q:
            curr = q.popleft()
            for move in range(1, 7):
                nxt = curr + move
                if nxt >= n * n:
                    continue
                dest = cells[nxt] if cells[nxt] != -1 else nxt
                if visited[dest] == -1:
                    visited[dest] = visited[curr] + 1
                    if dest == n * n - 1:
                        return visited[dest]
                    q.append(dest)

        return -1
