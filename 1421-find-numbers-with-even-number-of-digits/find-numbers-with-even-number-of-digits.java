class Solution {
    public int findNumbers(int[] nums) {
        int cnt = 0;

        for (int num : nums) {
            int dgts = (int) Math.log10(num) + 1;
            if (dgts % 2 == 0) {
                cnt++;
            }
        }

        return cnt;
    }
}