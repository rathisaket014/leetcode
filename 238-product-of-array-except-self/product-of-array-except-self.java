class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];

        Arrays.fill(res, 1);

        int pre = 1; 
        int post = 1;

        for (int i = 0; i < nums.length; i++) {
            res[i] = pre;
            pre = nums[i] * pre; 
        }

        for (int j = nums.length - 1; j >= 0; j--) {
            res[j] *= post;
            post = post * nums[j];
        }

        return res;

    }
}