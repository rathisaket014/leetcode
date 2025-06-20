class Solution {
    public int maxDistance(String s, int k) {
        int N = 0, S = 0, E = 0, W = 0;
        int maxD = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'N')
                N++;
            else if (c == 'S')
                S++;
            else if (c == 'E')
                E++;
            else if (c == 'W')
                W++;

            int dist = Math.abs(N - S) + Math.abs(E - W) + 2 * k;
            maxD = Math.max(maxD, Math.min(dist, i + 1));
        }
        return maxD;
    }
}