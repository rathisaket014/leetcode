class Solution {
    public boolean divideArray(int[] nums) {
        Map<Integer, Integer> frq = new HashMap<>();

        for (int num : nums) {
            frq.put(num, frq.getOrDefault(num, 0) + 1);
        }

        for (int count : frq.values()) {
            if (count % 2 != 0) return false;
        } 

        return true;
    }
}