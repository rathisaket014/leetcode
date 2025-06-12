class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
         n = len(nums)
         nums.append(nums[0])
         return max(abs(nums[i] - nums[i + 1]) for i in range(n))