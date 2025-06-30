class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = 0

        for i in cnt:
            if i + 1 in cnt:
                res = max(res, cnt[i] + cnt[i + 1])
        
        return res