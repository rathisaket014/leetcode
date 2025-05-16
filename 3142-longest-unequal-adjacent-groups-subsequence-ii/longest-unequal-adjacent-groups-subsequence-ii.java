class Solution {
    public boolean hammingDist(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int diff = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != t.charAt(i)) {
                diff++;
                if (diff > 1) return false;
            }
        }

        return diff == 1;
    }

    public List<String> getWordsInLongestSubsequence(String[] words, int[] groups) {
        int n = words.length;
        int[] dp = new int[n];
        int[] next = new int [n];

        Arrays.fill(dp, 1);
        Arrays.fill(next, -1);

        int len = 0, st = -1;

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                if (groups[i] != groups[j] && hammingDist(words[i], words[j])) {
                    if (dp[j] + 1 > dp[i]) {
                        dp[i] = dp[j] + 1;
                        next[i] = j;
                    }
                }
            }

            if (dp[i] > len) {
                len = dp[i];
                st = i;
            }
        }

        List<String> res = new ArrayList<>();
        while (st != -1) {
            res.add(words[st]);
            st = next[st];
        }

        return res;    
    }
}