class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;

        int max = 0;

        while (left < right) {
            int wid = right - left;
            int area = Math.min(height[left], height[right]) * wid;

            max = Math.max(max, area);

            if (height[left] <= height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return max;
    }
}