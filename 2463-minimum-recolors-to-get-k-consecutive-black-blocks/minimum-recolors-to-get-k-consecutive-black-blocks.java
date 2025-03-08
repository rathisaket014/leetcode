class Solution {
    public int minimumRecolors(String blocks, int k) {
        int n = blocks.length();
        int whites = 0;

        for (int i = 0; i < k; i++) {
            if (blocks.charAt(i) == 'W') {
                whites++;
            }
        }

        int res = whites;

        for (int i = k; i < n; i++) {
        if (blocks.charAt(i - k) == 'W') {
                whites--;
            }
            if (blocks.charAt(i) == 'W') {
                whites++;
            }

            res = Math.min(whites, res);
        }

        return res;
    }
}