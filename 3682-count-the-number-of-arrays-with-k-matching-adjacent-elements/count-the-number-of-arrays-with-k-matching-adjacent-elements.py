class Solution:
    mod = 10**9 + 7
    MAX = 10**5 + 10
    factorial = [1] + [0] * MAX
    Inv = [1] + [0] * MAX

    for i in range(1, MAX):
        factorial[i] = factorial[i - 1] * i % mod
        Inv[i] = pow(factorial[i], mod - 2, mod)

    def comb(self, m: int, n: int) -> int:
        return self.factorial[m] * self.Inv[n] * self.Inv[m - n] % self.mod

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return self.comb(n - 1, k) * m * pow(m - 1, n - k - 1, self.mod) % self.mod