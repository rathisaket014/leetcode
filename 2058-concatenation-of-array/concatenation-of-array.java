class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[2 * n];
        int i = 0;
        for (int num : nums) {
            ans[i] = num;
            ans[i + n] = num;
            i++;
        }

        return ans;
    }
}