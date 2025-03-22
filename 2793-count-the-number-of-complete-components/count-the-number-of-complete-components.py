class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        temp = [[] for i in range(n)]

        for u, v in edges:
            temp[u].append(v)
            temp[v].append(u)
        
        visited = [0] * n
        res = 0

        for i in range(n):
            if visited[i]:
                continue
            bfs = [i]
            visited[i] = 1
            for j in bfs:
                for k in temp[j]:
                    if visited[k] == 0:
                        bfs.append(k)
                        visited[k] = 1
            
            if all(len(temp[j]) == len(bfs) - 1 for j in bfs):
                res += 1

        return res 