class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def candies(n):
            if n < 0:
                return 0
            else:
                return (n + 2) * (n + 1) // 2
        
        return (candies(n)
                - 3 * candies(n - limit -1)
                + 3 * candies(n - 2 * (limit + 1))
                - candies(n - 3 * (limit + 1))
        )