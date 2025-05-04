class Solution {
    public int minDominoRotations(int[] tops, int[] bottoms) {
        int n = tops.length, m = bottoms.length;
        if (n != m) {
            return -1;
        }

        int[] ntops = new int[7];
        int[] nbottoms = new int[7];
        int[] same = new int[7];

        for (int i = 0; i < n; i++) {
            ntops[tops[i]]++;
            nbottoms[bottoms[i]]++;

            if (tops[i] == bottoms[i]) {
                same[tops[i]]++;
            }
        }

        int res = Integer.MAX_VALUE;

        for (int j = 1; j <= 6; j++) {
            if (ntops[j] + nbottoms[j] - same[j] == n) {
                res = Math.min(res, Math.min(n - ntops[j], n - nbottoms[j]));
            }
        }

        return res == Integer.MAX_VALUE ? -1 : res;
    }
}