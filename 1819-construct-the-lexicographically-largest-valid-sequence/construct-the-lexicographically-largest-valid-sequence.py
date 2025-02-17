class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        seq = [0] * (2 * n - 1)
        seen = set()
        def dfs(i):
            if i == len(seq):
                return True
            if seq[i]:
                return dfs(i + 1)
            for j in range(n, 0, -1):
                if j in seen:
                    continue
                seen.add(j)
                seq[i] = j
                if j == 1:
                    if dfs(i + 1):
                        return True
                elif i + j < len(seq) and seq[i + j] == 0:
                    seq[i + j] = j
                    if dfs(i + 1):
                        return True
                    seq[i + j] = 0
                seq[i] = 0
                seen.remove(j)
            return False
        dfs(0)
        return seq