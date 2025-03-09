class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        size = n + k - 1

        ans = 0
        temp = 1
        prev = colors[0]

        for i in range(1, size):
            j = i % n
            temp = 1 if prev == colors[j] else temp + 1
            ans += (temp >= k)
            prev = colors[j]
        
        return ans
            