class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        total = [0] * n
        prev = questions[-1][0]

        for i in range(n - 1, -1, -1):
            total[i] = prev
            pt, skip = questions[i]
            j = i + skip + 1

            if j < n:
                pt += total[j]
            if pt > prev:
                total[i] = pt
            prev = total[i]
        
        return total[0]