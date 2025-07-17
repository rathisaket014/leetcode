class Solution {
    public int findDuplicate(int[] nums) {
        int slw = nums[0];
        int fst = nums[0];

        do {
            slw = nums[slw];
            fst = nums[nums[fst]];
        } while(slw != fst);

        slw = nums[0];

        while(slw != fst) {
            slw = nums[slw];
            fst = nums[fst];
        }

        return slw;
    }
}