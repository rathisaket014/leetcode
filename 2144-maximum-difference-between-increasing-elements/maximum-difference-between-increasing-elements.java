class Solution {
    public int maximumDifference(int[] nums) {
        int res = 0;

        int left = Integer.MAX_VALUE;
        int right = 0;

        for (int i : nums) {
            left = Math.min(left, i);
            res = Math.max(res, i - left);
        }

        if (res > 0) {
            return res;
        }
        return -1;
    }
}