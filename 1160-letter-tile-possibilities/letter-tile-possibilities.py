class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = tuple(sorted(Counter(tiles).values()))

        @cache
        def dfs(cnt):
            s = 0
            for i in range(len(cnt)):
                if cnt[i] == 0:
                    continue
                new = list(cnt)
                new[i] -= 1
                s += 1 + dfs(tuple(new))
            return s
        return dfs(cnt)