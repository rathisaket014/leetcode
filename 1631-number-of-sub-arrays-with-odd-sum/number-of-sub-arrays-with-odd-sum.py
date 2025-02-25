class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        odd = 0
        even = 1

        pf_sum = 0
        ans = 0

        for i in arr:
            pf_sum += i
            if pf_sum % 2 == 0:
                ans = (ans + odd) % mod
                even += 1
            else:
                ans = (ans + even) % mod
                odd += 1
        
        return ans