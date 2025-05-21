class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        st = 0
        max_len = 0

        for en in range(len(s)):
            while s[en] in char_set:
                char_set.remove(s[st])
                st += 1
            char_set.add(s[en])
            max_len = max(max_len, en - st + 1)
            
        return max_len

        # sliding window technique