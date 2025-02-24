class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        Path = {}
        visited = set()

        def Bob(node, time):
            visited.add(node)
            Path[node] = time
            if node == 0:
                return True
            
            for nei in adj[node]:
                if nei not in visited and Bob(nei, time + 1):
                    return True
            
            Path.pop(node)
            return False

        Bob(bob, 0)
        visited.clear()
        maxProft = float('-inf')

        def Alice(node, time, income):
            nonlocal maxProft
            visited.add(node)

            if node not in Path or time < Path[node]:
                income += amount[node]
            elif time == Path[node]:
                income += amount[node] // 2
            

            if len(adj[node]) == 1 and node != 0:
                maxProft = max(maxProft, income)
            
            for nei in adj[node]:
                if nei not in visited:
                    Alice(nei, time + 1, income)
        
        Alice(0, 0, 0)
        return maxProft
