class Solution {
    public int[] applyOperations(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];

        for (int i = 0; i < n - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
        }
        
        int idx = 0;

        for (int num : nums) {
            if (num != 0) {
                ans[idx++] = num;
            }
        }

        while(idx < n) {
            ans[idx++] = 0;
        }

        return ans;
    }
}