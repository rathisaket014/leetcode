class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = 'aeiou'
        vowset = set(vowels)
        vowCnt = defaultdict(int)

        cons = 0
        left = count = substr = 0

        def minus(ch):
            if ch in vowset:
                vowCnt[ch] -= 1
                if vowCnt[ch] == 0:
                    del vowCnt[ch]
            else:
                nonlocal cons
                cons -= 1
        
        for ch in word:
            if ch in vowset:
                vowCnt[ch] += 1
            else:
                cons += 1
                count = 0
            
            while cons > k:
                minus(word[left])
                left += 1
            while cons == k and len(vowCnt) == 5:
                count += 1
                minus(word[left])
                left += 1
            substr += count
        
        return substr