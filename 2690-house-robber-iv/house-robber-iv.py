class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        minHouse = min(nums)
        maxHouse = max(nums)

        def money(capability):
            steal, i = 0, 0
            while i < n and steal < k:
                if nums[i] <= capability:
                    steal += 1
                    i += 1
                i += 1
            return steal >= k
        
        low, high = minHouse, maxHouse
        while low < high:
            mid = (low + high) >> 1
            if money(mid):
                high = mid
            else:
                low = mid + 1
        
        return low