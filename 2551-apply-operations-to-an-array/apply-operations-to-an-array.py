class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n - 1):
            if (nums[i] == nums[i + 1]):
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
        
        for i in nums:
            if i != 0:
                ans.append(i)
        
        while len(ans) < n:
            ans.append(0)

        return ans