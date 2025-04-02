class Solution {
    public long maximumTripletValue(int[] nums) {
        int n = nums.length;
        long res = Integer.MIN_VALUE;

        if (n < 3) return 0;

        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    long curr = (long)(nums[i] - nums[j]) * nums[k];
                    res = Math.max(res, curr);
                }
            }
        }

        return res > 0 ? res : 0;
    }
}