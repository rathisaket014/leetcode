class Solution {
    public int removeDuplicates(int[] nums) {
        int res = 0;
        int n = nums.length;

        int i = 0;

        for (int j = 1; j < n; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        
        res = i + 1;
        return res;
    }
}