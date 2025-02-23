class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int l = 2 * n;
        int[] ans = new int[l];
        int i = 0;
        for (int num : nums) {
            ans[i] = num;
            ans[i + n] = num;
            i++;
        }

        return ans;
    }
}