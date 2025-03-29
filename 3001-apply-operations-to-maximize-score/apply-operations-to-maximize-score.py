@lru_cache(None)
def isPrimeScore(num):
    score = 0
    if num % 2 == 0:
        score += 1
        while num % 2 == 0:
            num //= 2
    
    for p in range(3, int(sqrt(num)) + 1, 2):
        if num % p == 0:
            score += 1
        while num % p == 0:
            num //= p
    
    if num > 1:
        score += 1
    
    return score

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        # Compute scores for each num, and add a sentinel at the end.
        scores = [isPrimeScore(num) for num in nums] + [MOD]

        # Compute left bounds using a monotonic stack.
        lefts = [0] * n
        stack = [-1]
        for i in range(n):
            while stack[-1] != -1 and scores[i] > scores[stack[-1]]:
                stack.pop()
            lefts[i] = stack[-1]
            stack.append(i)

        # Compute right bounds using a monotonic stack.
        rights = [0] * n
        stack = [n]
        for i in range(n - 1, -1, -1):
            while stack[-1] != n and scores[i] >= scores[stack[-1]]:
                stack.pop()
            rights[i] = stack[-1]
            stack.append(i)

        max_score = 1
        # Process numbers in descending order.
        for num, i in sorted(((num, i) for i, num in enumerate(nums)), reverse=True):
            count = (i - lefts[i]) * (rights[i] - i)
            use = min(k, count)
            max_score = (max_score * pow(num, use, MOD)) % MOD
            if count >= k:
                break
            k -= count

        return max_score