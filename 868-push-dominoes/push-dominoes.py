class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        temp = [0] * n
        i = 0

        for j in range (n - 1, -1, -1):
            c = dominoes[j]
            if c == 'L':
                i = n
            elif c == 'R':
                i = 0
            elif c == '.':
                if i > 0:
                    i -= 1
            temp[j] = i
        i = 0
        dominoes = list(dominoes)

        for j in range(n):
            c = dominoes[j]
            if c == 'L':
                i = 0
            elif c == 'R':
                i = n
            elif c == '.':
                if i > 0:
                    i -= 1
                if i < temp[j]:
                    dominoes[j] = 'L'
                elif i > temp[j]:
                    dominoes[j] = 'R'
        
        return ''.join(dominoes)