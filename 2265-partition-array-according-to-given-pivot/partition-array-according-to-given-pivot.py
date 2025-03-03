class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        pf = [0] * n
        left, right = 0, n - 1

        for i, j in zip(range(n), range(n - 1, -1, -1)):
            if nums[i] < pivot:
                pf[left] = nums[i]
                left += 1
            if nums[j] > pivot:
                pf[right] = nums[j]
                right -= 1
        
        while left <= right:
            pf[left] = pivot
            left += 1
        
        return pf