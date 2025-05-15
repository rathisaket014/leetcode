class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        res = [words[0]]

        i = 0

        while i < n:
            while i < n and groups[0] == groups[i]:
                i += 1
            if i < n:
                res.append(words[i])
                groups[0] = groups[i]
            i += 1
        
        return res