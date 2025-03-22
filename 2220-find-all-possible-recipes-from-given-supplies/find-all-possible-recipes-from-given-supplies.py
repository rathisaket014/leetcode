class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        supply = set(supplies)
        deg = [0] * n
        adj = defaultdict(list)

        for i in range(n):
            for j in ingredients[i]:
                if j not in supply:
                    adj[j].append(i)
                    deg[i] += 1
        
        que = deque()
        for i in range(n):
            if deg[i] == 0:
                que.append(i)
        
        res = []

        while que:
            i = que.popleft()
            res.append(recipes[i])
            for j in adj[recipes[i]]:
                deg[j] -= 1
                if deg[j] == 0:
                    que.append(j)
        
        return res