class Solution {
    public int[] maxPoints(int[][] grid, int[] queries) {
        int row = grid.length, col = grid[0].length;
        int n = queries.length;
        int[] res = new int[n];

        // sorted queries array
        int[][] sq = new int[n][2];
        for (int i = 0; i < n; i++) {
            sq[i][0] = queries[i];
            sq[i][1] = i;
        }

        // sort queries by the query value
        Arrays.sort(sq, (a, b) -> Integer.compare(a[0], b[0]));

        // priority queue (min-heap) for cells
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        heap.offer(new int[] {grid[0][0], 0, 0});

        grid[0][0] = 0;

        int count = 0;

        int[] dr = {-1, 0, 0, 1};
        int[] dc = {0, 1, -1, 0};

        // processing each query in inc order
        for (int[] pair : sq) {
            int q = pair[0];
            int idx = pair[1];

            while (!heap.isEmpty() && heap.peek()[0] < q) {
                int[] curr = heap.poll();
                int curVal = curr[0];
                int r = curr[1], c = curr[2];

                count++;

                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    if (nr >= 0 && nr < row && nc >= 0 && nc < col && grid[nr][nc] != 0) {
                        heap.offer(new int[]{grid[nr][nc], nr, nc});

                        grid[nr][nc] = 0;
                    }
                }
            }

            res[idx] = count;
        }

        return res;
    }
}