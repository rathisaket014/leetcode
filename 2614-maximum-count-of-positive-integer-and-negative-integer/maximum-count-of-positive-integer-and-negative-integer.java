class Solution {
    public int maximumCount(int[] nums) {
        int n = nums.length;

        int pcount = 0;
        int ncount = 0;

        for (int num : nums) {
            if (num > 0) {
                pcount++;
            } else if(num < 0) {
                ncount++;
            }
        }

        return Math.max(pcount, ncount);
    }
}