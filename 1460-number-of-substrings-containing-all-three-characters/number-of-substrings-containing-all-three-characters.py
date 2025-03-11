class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = [0] * 3
        left = 0
        ans = 0

        for i, char in enumerate(s):
            count[ord(char) - ord('a')] += 1

            while all(count):
                ans += len(s) - i
                count[ord(s[left]) - ord('a')] -= 1
                left += 1

        return ans