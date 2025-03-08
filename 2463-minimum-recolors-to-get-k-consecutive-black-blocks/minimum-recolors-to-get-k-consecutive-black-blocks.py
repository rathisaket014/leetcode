class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        whites = 0

        for i in range(0, k):
            if blocks[i] == 'W':
                whites += 1
        
        count = whites
        
        for i in range(k, n):
            if blocks[i - k] == 'W':
                whites -= 1
            if blocks[i] == 'W':
                whites += 1
            count = whites if whites < count else count
        
        return count