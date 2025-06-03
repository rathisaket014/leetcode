class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        l = set()
        res = 0
        prev = None

        while res != prev:
            prev = res
            q = []

            for curr in initialBoxes:
                if curr in l or status[curr]:
                    res += candies[curr]
                    l.update(keys[curr])
                    q.extend(containedBoxes[curr])
                else:
                    q.append(curr)
            initialBoxes = q
        
        return res