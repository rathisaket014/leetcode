class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> k = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int l = target - nums[i];

            if (k.containsKey(l)) {
                return new int[] { k.get(l), i };
            }

            k.put(nums[i], i);
        }

        return new int[] {};
    }
}