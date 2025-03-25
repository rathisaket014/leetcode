class Solution {
    public boolean containsDuplicate(int[] nums) {
        int n = nums.length;
        HashMap<Integer, Integer> set = new HashMap<>();

        for (int num : nums) {
            set.put(num, set.getOrDefault(num, 0) + 1);
        }

        for (int key : set.keySet()) {
            if (set.get(key) > 1) {
                return true;
            }
        }

        return false;
    }
}