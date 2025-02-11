class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        curr = [] # empty list
        n = len(part) # len of pattern
        end = part[-1] # end char of pattern

        for i in s:
            curr.append(i) # appending character in empty list
            if i == end and len(curr) >= n: # while iterating if i is the end ch of that pattern and the len of the curr list is >= n that means its possible substr exists
                if "".join(curr[-n:]) == part: # traverse backwards in curr to see if substr matches
                    del curr[-n:] # if yes the delete it from curr
        return "".join(curr) # return whatever's left