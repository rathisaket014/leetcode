class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        
        n = len(word)
        m = n - numFriends + 1

        i = 0
        j = 1

        while j < n:
            k = 0
            while j + k < n and word[i + k] == word[j + k]:
                k += 1

            if j + k < n and word[i + k] < word[j + k]:
                i, j = j, max(j + 1, i + k + 1)
            else:
                j += k + 1
        
        res = word[i:]

        return res if len(res) <= m else res[:m]