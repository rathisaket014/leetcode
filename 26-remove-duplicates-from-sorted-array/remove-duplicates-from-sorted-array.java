class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;
        
        if (n == 0) {
            return 0;
        }

        int idx = 0;

        for (int i = 1; i < n; i++) {
            if (nums[i] != nums[idx]) {
                idx++;
                nums[idx] = nums[i];
            }
        }

        return idx + 1;
    }
}