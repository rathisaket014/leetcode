class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        
        idx = 0

        for i in range(1, n):
            if nums[i] != nums[idx]:
                idx += 1
                nums[idx] = nums[i]

        return idx + 1