class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def pair(x):
            cnt = 0
            for n1 in nums1:
                if n1 > 0:
                    cnt += bisect.bisect_right(nums2, x // n1)
                elif n1 < 0:
                    cnt += len(nums2) - bisect_left(nums2, ceil(x / n1))
                elif x >= 0:
                    cnt += len(nums2)
            return cnt

        st = -(10**10) - 1
        en = 10**10 + 1
        while st + 1 < en:
            mid = (st + en) // 2
            if pair(mid) >= k:
                en = mid
            else:
                st = mid
        return st + 1
