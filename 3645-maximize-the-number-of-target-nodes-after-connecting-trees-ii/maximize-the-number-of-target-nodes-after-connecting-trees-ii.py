class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def find_even(edges: list, n: int) -> list:
            adj = [[] for _ in range(n)]
            q =  deque([(0, -1, True)])

            evenlist = [False] * n

            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u) 

            while q:
                node, parent, is_even = q.popleft()
                evenlist[node] = is_even
                for c in adj[node]:
                    if c == parent:
                        continue
                    q.append((c, node, not is_even))
            
            return evenlist
        
        l1 = len(edges1) + 1
        l2 = len(edges2) + 1

        e1, e2 = find_even(edges1, l1), find_even(edges2, l2)

        t1, t2 = sum(e1), sum(e2)

        mx = max(t2, l2 - t2)

        res = [mx + (t1 if even else l1 - t1) for even in e1]
        
        return res