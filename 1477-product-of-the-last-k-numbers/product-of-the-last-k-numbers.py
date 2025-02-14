class ProductOfNumbers:
    arr = []
    def __init__(self):
        self.arr.append(1)

    def add(self, num: int) -> None:
        if num == 0:
            self.arr = []
            self.arr.append(1)
        else:
            self.arr.append(self.arr[-1] * num)

    def getProduct(self, k: int) -> int:
        if k > len(self.arr) - 1:
            return 0
        else:
            return self.arr[-1] // self.arr[-1 - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)