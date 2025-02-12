class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_of_digits(i):
            res = 0
            while i:
                res += i % 10
                i //= 10
            return res
        
        pairs = defaultdict(list)
        for num in nums:
            key = sum_of_digits(num)
            pairs[key].append(num)

        max_sum = -1
        for p in pairs:
            if len(pairs[p]) > 1:
                temp = sorted(pairs[p], reverse=True)[:2]
                max_sum = max(max_sum, sum(temp))
        
        return max_sum