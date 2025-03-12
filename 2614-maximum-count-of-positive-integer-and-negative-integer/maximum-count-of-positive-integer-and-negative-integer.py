class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        posc, negc = 0, 0
        for i in nums:
            if i > 0:
                posc += 1
            if i < 0:
                negc += 1
            else:
                continue
        
        return max(posc, negc)