class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(num: str, target: int) -> bool:
            if not num:
                return target == 0
            
            for i in range(1, len(num) + 1):
                part = int(num[:i])
                if part > target:
                    break
                if partition(num[i:], target - part):
                    return True
            
            return False
        
        res = 0

        for i in range(1, n + 1):
            sq = i * i
            if partition(str(sq), i):
                res += sq
            
        return res
                