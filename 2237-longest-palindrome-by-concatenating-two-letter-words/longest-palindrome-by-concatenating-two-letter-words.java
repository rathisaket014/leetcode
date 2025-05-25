class Solution {
    public int longestPalindrome(String[] words) {
        int[][] frq = new int[26][26];

        for(String w : words) {
            int a = w.charAt(0) - 'a';
            int b = w.charAt(1) - 'a';

            frq[a][b]++;
        }

        int sum = 0;
        boolean center = false;

        for (int i = 0; i < 26; i++) {
            sum += (frq[i][i] / 2) * 4;
            if (frq[i][i] % 2 == 1) {
                center = true;
            }

            for (int j = i + 1; j < 26; j++) {
                int pairs = Math.min(frq[i][j], frq[j][i]);
                sum += pairs * 4;
            }
        }

        if (center) {
            sum += 2;
        }

        return sum;
    }
}