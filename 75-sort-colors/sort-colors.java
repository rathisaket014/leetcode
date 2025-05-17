class Solution {
    public void sortColors(int[] nums) {
        int r = 0, w = 1, b = 2;
        int st = 0, mid = 0, en = nums.length - 1;

        while (mid <= en) {
            int i = nums[mid];
            if (i == r) {
                int temp = nums[st];
                nums[st] = nums[mid];
                nums[mid] = temp;

                st++;
                mid++;
            } else if (i == w) {
                mid++;
            } else {
                int temp = nums[mid];
                nums[mid] = nums[en];
                nums[en] = temp;
                en--;
            }
        }
    }
}