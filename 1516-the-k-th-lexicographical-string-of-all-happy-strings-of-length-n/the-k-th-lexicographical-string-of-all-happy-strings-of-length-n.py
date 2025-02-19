class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (1 << (n - 1))

        if k > total:
            return ""
        
        st = ['a', 'b', 'c']
        res = []
        k -= 1
        for i in range(n):
            blk = 1 << (n - i - 1)
            idx = k // blk
            for ch in st:
                if not res or ch != res[-1]:
                    if idx == 0:
                        res.append(ch)
                        break
                    idx -= 1    
            k %= blk
        return "".join(res)