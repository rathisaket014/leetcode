class Solution {
    public int[] queryResults(int limit, int[][] queries) {
        int dis = 0;
        
        Map<Integer, Integer> frq = new HashMap<>();
        Map<Integer, Integer> colors = new HashMap<>();

        int n = queries.length;
        int[] res = new int[n];

        for (int i = 0; i < n; i++) {
            int ball = queries[i][0];
            int color = queries[i][1];

            frq.put(color, frq.getOrDefault(color, 0) + 1);
            
            if (frq.get(color) == 1) {
                dis++;
            }

            if (colors.containsKey(ball)) {
                int old = colors.get(ball);
                frq.put(old, frq.get(old) - 1);

                if (frq.get(old) == 0) {
                    dis--;
                }
            }

            colors.put(ball, color);
            res[i] = dis;
        }

        return res;
    }
}