class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        res = []
        
        nums.sort()

        for i in range(0, n, 3):
            g = [nums[i], nums[i + 1], nums[i + 2]]
            if g[2] - g[0] > k:
                return []
            res.append(g)
        
        return res