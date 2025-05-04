class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = defaultdict(int)
        for domino in dominoes:
            eq = min(domino[0], domino[1]) * 10 + max(domino[0], domino[1])
            counter[eq] += 1
        
        return sum(count * (count - 1) // 2 for count in counter.values())