class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        length = 0
        left = 0

        for right, i in enumerate(nums):
            while left < right and (length & i) != 0:
                length ^= nums[left]
                left += 1
            length |= i
            res = max(res, right - left + 1)

        return res