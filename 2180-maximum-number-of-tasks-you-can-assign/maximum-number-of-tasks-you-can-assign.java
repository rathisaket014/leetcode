class Solution {
    public int maxTaskAssign(int[] tasks, int[] workers, int pills, int strength) {
        int lo = 0, hi = Math.min(tasks.length, workers.length);
        Arrays.sort(tasks);
        Arrays.sort(workers);

        while (lo < hi) {
            int midVal = (lo + hi + 1) / 2;
            int pillsUsed = 0;
            TreeMap<Integer, Integer> pool = new TreeMap<>();
            for (int i = workers.length - midVal; i < workers.length; ++i) {
                pool.put(workers[i], pool.getOrDefault(workers[i], 0) + 1);
            }

            boolean possible = true;
            for (int ti = midVal - 1; ti >= 0; --ti) {
                int requirement = tasks[ti];
                int strongest = pool.lastKey();
                if (strongest >= requirement) {
                    removeOne(pool, strongest);
                } else {
                    Integer boosted = pool.ceilingKey(requirement - strength);
                    if (boosted == null || ++pillsUsed > pills) {
                        possible = false;
                        break;
                    }
                    removeOne(pool, boosted);
                }
            }

            if (possible) {
                lo = midVal;
            } else {
                hi = midVal - 1;
            }
        }

        return lo;
    }

    private void removeOne(TreeMap<Integer, Integer> map, int key) {
        int count = map.get(key);
        if (count == 1) {
            map.remove(key);
        } else {
            map.put(key, count - 1);
        }
    }
}
