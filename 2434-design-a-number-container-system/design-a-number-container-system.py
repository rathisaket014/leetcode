class NumberContainers:

    def __init__(self):
        self.itonum = {}  # index to number
        self.numtoi = defaultdict(SortedSet) # number to index sorted set
 
    def change(self, index: int, number: int) -> None:
        if index in self.itonum:
            oldno = self.itonum[index]
            self.numtoi[oldno].discard(index)
            if not self.numtoi[oldno]:
                del self.numtoi[oldno]
        
        self.itonum[index] = number
        self.numtoi[number].add(index)

    def find(self, number: int) -> int:
        if number in self.numtoi and self.numtoi[number]:
            return self.numtoi[number][0]
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)