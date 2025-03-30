class Solution {
    public int countValidSelections(int[] nums) {
        int n = nums.length;
        int count = 0, ls = 0, rs = 0, i;

        // Find the first occurrence of 0 and calculate left sum
        for (i = 0; i < n; i++) {
            if (nums[i] == 0) break;
            ls += nums[i];
        }

        // Calculate right sum
        for (int j = i + 1; j < n; j++) {
            rs += nums[j];
        }

        // Iterate from the first zero found
        for (int k = i; k < n; k++) {
            ls += nums[k];  // Add current element to left sum
            rs -= nums[k];  // Remove current element from right sum

            // Only process when the element is 0
            if (nums[k] != 0) continue;

            if (ls == rs) {
                count += 2;  // Both left and right are valid
            } else if (ls - 1 == rs || ls + 1 == rs) {
                count += 1;  // One of them is valid
            }
        }

        return count;
    }
}
