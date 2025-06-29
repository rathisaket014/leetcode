class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7

        n = len(nums)
        nums.sort()

        st, en = 0, n - 1

        res = 0

        while st <= en:
            if nums[st] + nums[en] <= target:
                res += pow(2, en - st, mod)
                res %= mod
                st += 1
            else:
                en -= 1
        
        return res