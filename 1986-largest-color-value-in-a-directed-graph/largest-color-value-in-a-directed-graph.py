class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dest in edges:
            adj[src].append(dest)
        
        def dfs(node):
            if node in path:
                return float("inf")
            
            if node in visited:
                return 0
            
            visited.add(node)
            path.add(node)

            idx = ord(colors[node]) - ord('a')
            count[node][idx] = 1

            for neigh in adj[node]:
                if dfs(neigh) == float("inf"):
                    return float("inf")
                
                for col in range(26):
                    count[node][col] = max(count[node][col], (1 if col == idx else 0) + count[neigh][col])
                
            path.remove(node)
            return max(count[node])

        n = len(colors)
        res = 0

        visited, path = set(), set()
        count = [[0] * 26 for i in range(n)] # matrix[node][color]

        for i in range(n):
            res = max(dfs(i), res)
        
        return -1 if res == float("inf") else res
