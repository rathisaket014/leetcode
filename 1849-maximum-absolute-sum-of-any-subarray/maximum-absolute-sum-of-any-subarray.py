class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxRes = 0
        minRes = 0

        for num in nums:
            maxRes = max(0, maxRes + num)
            minRes = min(0, minRes + num)
        
        return maxRes - minRes