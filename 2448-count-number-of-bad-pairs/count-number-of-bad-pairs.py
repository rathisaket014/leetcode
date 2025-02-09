class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        stg = {}
        aPair = 0

        for i, num in enumerate(nums):
            key = num - i
            aPair += stg.get(key, 0)
            stg[key] = stg.get(key, 0) + 1

        n = len(nums)
        return (n * (n - 1)) // 2 - aPair