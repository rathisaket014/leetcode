class Solution {
    public int tupleSameProduct(int[] nums) {
        int n = nums.length;

        Map<Integer, Integer> freq = new HashMap<>();

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int prod = nums[i] * nums[j];
                freq.put(prod, freq.getOrDefault(prod, 0) + 1);
            }
        }

        int res = 0;

        for (int f : freq.values()) {
            if (f > 1) {
                res += (f * (f - 1) / 2) * 8;
            }
        }

        return res;
    }
}