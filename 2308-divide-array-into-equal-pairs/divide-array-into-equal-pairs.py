class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        frq = Counter(nums)

        for count in frq.values():
            if count % 2 != 0:
                return False
        
        return True