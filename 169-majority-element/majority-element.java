class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> fq = new HashMap<>();

        for (int num : nums) {
            fq.put(num, fq.getOrDefault(num, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : fq.entrySet()) {
            if (entry.getValue() > nums.length / 2) {
                return entry.getKey();
            }
        }

        return -1; // This line should never be reached for valid inputs
    }
}