class Solution:
    def check(self, a, n):
        temp = [a[0]]
        
        for i in range(1, n):
            if a[i][0] >= temp[-1][1]:
                temp.append(a[i])
            else:
                temp[-1] = (temp[-1][0], max(temp[-1][1], a[i][1]))
        
        return len(temp) >= 3
    
    
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        l = len(rectangles)

        x, y = [], []
        for i in rectangles:
            x.append((i[0], i[2]))
            y.append((i[1], i[3]))
        x.sort()
        y.sort()

        return self.check(x, l) or self.check(y, l)