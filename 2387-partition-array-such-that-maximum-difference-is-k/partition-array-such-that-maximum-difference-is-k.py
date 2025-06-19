class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(set(nums))
        
        nums = sorted(list(set(nums)))

        ans = 0

        prev = -1

        for n in nums:
            if n > prev:
                prev = n
                ans += 1
                prev += k
            else:
                continue
        
        return ans