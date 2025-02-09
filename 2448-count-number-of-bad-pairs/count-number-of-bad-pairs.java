class Solution {
    public long countBadPairs(int[] nums) {
        long goodPairs = 0;

        Map<Long, Long> count = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            long key = (long) nums[i] - i;

            long cnt = count.getOrDefault(key, 0L);

            goodPairs += cnt;

            count.put(key, cnt + 1);
        } 

        long n = nums.length;

        long totalPairs = (n * (n - 1)) / 2;

        return totalPairs - goodPairs;
    }
}