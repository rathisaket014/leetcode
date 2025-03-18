class Solution {
    public int longestNiceSubarray(int[] nums) {
        int n = nums.length;
        int left = 0;
        int mask = 0;
        int ans = 0;
        
        for (int right = 0; right < n; right++) {
            // While there is a conflict with nums[right], shrink the window.
            while ((mask & nums[right]) != 0) {
                // Remove the leftmost element's bits from the mask.
                mask &= ~nums[left];
                left++;
            }
            // Add the current number to the mask.
            mask |= nums[right];
            // Update the maximum length.
            ans = Math.max(ans, right - left + 1);
        }
        
        return ans;   
    }
}