class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        d1 = [-1] * n
        d2 = [-1] * n

        def DFS(st: int, dist: List[int]):
            curr = st

            d = 0

            while curr != -1 and dist[curr] == -1:
                dist[curr] = d
                d += 1
                curr = edges[curr]
        

        DFS(node1, d1)
        DFS(node2, d2)

        res = -1

        min_dist = float('inf')

        for i in range(n):
            if d1[i] != -1 and d2[i] != -1:
                max_dist = max(d1[i], d2[i])

                if max_dist < min_dist or (max_dist == min_dist and i < res):
                    min_dist = max_dist
                    res = i
        

        return res