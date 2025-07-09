class Solution {
    public void moveZeroes(int[] nums) {
        /*
        0 1 0 3 12
        i j
        1 0 0 3 12
          i   j
        1 3 0 0 12
            i   j
        1 3 12 0 0
         */

        if (nums.length == 1) {
            return;
        }

        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[i] != 0) i++;
            if (nums[j] == 0 && j < nums.length - 1) j++;
            if (nums[i] == 0 && nums[j] != 0) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
    }
}