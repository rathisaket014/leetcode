class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(num: int) -> bool:
            if num <= 1:
                return False
            if num == 2:
                return True
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    return False
            
            return True
        
        res = []
        prime = None

        for i in range(left, right + 1):
            if not isPrime(i):
                continue
            if prime is None:
                prime = i
                continue
            diff = i - prime
            if diff <= 2:
                return [prime, i]
            if not res or diff < res[1] - res[0]:
                res = [prime, i]
            prime = i

        return res or [-1, -1]
