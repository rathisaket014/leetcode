class Solution {
    public int maxAbsoluteSum(int[] nums) {
        int max_sum = 0;
        int min_sum = 0;

        for (int num : nums) {
            max_sum = Math.max(0, max_sum + num);
            min_sum = Math.min(0, min_sum + num);
        }

        return max_sum - min_sum;
    }
}