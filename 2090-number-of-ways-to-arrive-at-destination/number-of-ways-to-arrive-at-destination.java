class Solution {
    static class Node implements Comparable<Node> {
        int id;
        long dist;

        public Node(int id, long dist) {
            this.id = id;
            this.dist = dist;
        }

        public int compareTo(Node other) {
            return Long.compare(this.dist, other.dist);
        }
    }

    public int countPaths(int n, int[][] roads) {
        // creating the graph
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        for(int[] road : roads) {
            int u = road[0], v = road[1], time = road[2];
            graph.get(u).add(new int[]{v, time});
            graph.get(v).add(new int[]{u, time});
        }

        // arr for shortest dist and ways
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        
        int[] ways = new int[n];
        int mod = 1_000_000_007;

        dist[0] = 0;
        ways[0] = 1;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(0, 0));

        while (!pq.isEmpty()) {
            Node curr = pq.poll();
            int u = curr.id;
            long d = curr.dist;

            if (d != dist[u]) continue;

            for (int[] edge : graph.get(u)) {
                int v = edge[0];
                int t = edge[1];
                long newDist = d + t;

                if (newDist < dist[v]) {
                    dist[v] = newDist;
                    ways[v] = ways[u];
                    pq.offer(new Node(v, newDist));
                } else if (newDist == dist[v]) {
                    ways[v] = (ways[v] + ways[u]) % mod;
                }
            }
        }

        return ways[n - 1];
    }
}