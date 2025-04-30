class Solution {
    public int findNumbers(int[] nums) {
        int cnt = 0;

        // for (int num : nums) {
        //     int dgts = (int) Math.log10(num) + 1;
        //     if (dgts % 2 == 0) {
        //         cnt++;
        //     }
        // }

        // given the constraints 
        for (int num : nums) {
            if ((num > 9 && num < 100) || (num > 999 && num < 10000) || (num == 100000)) {
                cnt++;
            }
        }

        return cnt;
    }
}