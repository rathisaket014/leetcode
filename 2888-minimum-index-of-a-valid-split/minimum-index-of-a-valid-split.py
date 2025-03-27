class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        idx = -1

        for i in nums:
            if cnt == 0:
                idx = i
            cnt += 1 if i == idx else -1
        
        fq = Counter(nums)
        cntFq = 0

        for i in range(n):
            cntFq += nums[i] == idx
            if cntFq * 2 > (i + 1) and (fq[idx] - cntFq) * 2 > (n - i - 1):
                return i

        return -1 