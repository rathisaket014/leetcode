class Solution {
    public int minOperations(int[] nums) {
        int n = nums.length;
        int cnt = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                cnt += 1;
                if (i + 1 >= n || i + 2 >= n) {
                    return -1;
                }
                nums[i] ^= 1;
                nums[i + 1] ^= 1;
                nums[i + 2] ^= 1;
            }
        }

        return cnt;
    }
}