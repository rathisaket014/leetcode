class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low = 1
        high = max(ranks) * cars * cars

        def canFix(t):
            total = sum(int(sqrt(t // r)) for r in ranks)
            return total >= cars
        
        while low < high:
            mid = (high + low) // 2
            if canFix(mid):
                high = mid
            else:
                low = mid + 1
        
        return low