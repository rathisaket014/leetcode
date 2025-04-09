class Solution {
    public int minOperations(int[] nums, int k) {
        boolean[] arr = new boolean[101];
        for (int num : nums) {
            arr[num] = true;
        }

        int cnt = 0;
        for (int i = 0; i < arr.length; i++) {
            if (!arr[i]) {
                continue;
            }
            if (arr[i] && i < k) {
                return -1;
            } else if (arr[i] && i > k) {
                cnt++;
            }
        }

        return cnt;   
    }
}