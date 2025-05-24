class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        sol = []

        for idx, word in enumerate(words):
            if word.find(x) != -1:
                sol.append(idx)
        
        return sol