class Solution:
    def UnionNode(self, node, parent):
        if parent[node] < 0:
            return node
        parent[node] = self.UnionNode(parent[node], parent)
        return parent[node]

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parent = [-1] * n
        cost = [-1] * n

        for u, v, w in edges:
            ru = self.UnionNode(u, parent)        
            rv = self.UnionNode(v, parent)
            if ru != rv:
                cost[ru] &= cost[rv]
                parent[rv] = ru
            cost[ru] &= w

        res = []

        for u, v in query:
            ru = self.UnionNode(u, parent)        
            rv = self.UnionNode(v, parent)        
            if u == v:
                res.append(0)
            elif ru != rv:
                res.append(-1)
            else:
                res.append(cost[ru])
            
        return res