class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int n = nums.length;
        int[] res = new int[n];
        int st = 0;
        int en = n - 1;

        for (int i = 0, j = n - 1; i < n; i++, j--) {
            if (nums[i] < pivot) {
                res[st++] = nums[i];
            }

            if (nums[j] > pivot) {
                res[en--] = nums[j];
            }
        }

        while (st <= en) {
            res[st++] = pivot;
        }

        return res;
    }
}