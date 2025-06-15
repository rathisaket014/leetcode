class Solution:
    def maxDiff(self, num: int) -> int:
        ten = [1] * 10
        for i in range(1, 10):
            ten[i] = ten[i - 1] * 10
        value = next(i for i in ten if i > num) // 10

        a, b = -1, -1
        x, y = 0, 0

        c = 0 if num // value == 1 else 1

        while value >= 1:
            d = num // value
            num %= value
            if a == -1 and d != 9:
                a = d
                x += 9 * value
            elif d == a:
                x += 9 * value
            else:
                x += d * value

            if b == -1 and d != 0 and d != 1:
                b = d
                y += c * value
            elif d == b:
                y += c * value
            else:
                y += d * value

            value //= 10

        return x - y