class Solution {
    public int[] constructDistancedSequence(int n) {
        int len = 2 * n - 1;
        int[] seq = new int[len];

        boolean[] used = new boolean[n + 1];

        dfs(0, seq, used, n);
        return seq;
    }

    private boolean dfs(int index, int[] seq, boolean[] used, int n) {
        if (index == seq.length) {
            return true;
        }

        if (seq[index] != 0) {
            return dfs(index + 1, seq, used, n);
        }

        for (int j  = n; j >= 1; j--) {
            if (used[j]) {
                continue;
            }

            used[j] = true;
            seq[index] = j;

            if (j == 1) {
                if (dfs(index + 1, seq, used, n)) {
                    return true;
                }
            } else {
                if (index + j < seq.length && seq[index + j] == 0) {
                    seq[index + j] = j;
                    if (dfs(index + 1, seq, used, n)) {
                        return true;
                    }

                    seq[index + j] = 0;
                }
            }

            seq[index] = 0;
            used[j] = false;
        }
        return false;
    }
}