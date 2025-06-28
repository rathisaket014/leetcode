class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        idx = [(num, i) for i, num in enumerate(nums)]

        minH = sorted(idx, key = lambda x: x[0], reverse=True)[:k]

        minH.sort(key = lambda x: x[1])

        return [num for num, _ in minH]