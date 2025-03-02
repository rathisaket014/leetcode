class Solution {
    public int[][] mergeArrays(int[][] nums1, int[][] nums2) {
        Map<Integer, Integer> mp = new HashMap<>();
        
        // for first array
        for (int[] i : nums1) {
            int id = i[0];
            int val = i[1];
            mp.put(id, mp.getOrDefault(id, 0) + val);
        }

        // for second array
        for (int[] j : nums2) {
            int id = j[0];
            int val = j[1];
            mp.put(id, mp.getOrDefault(id, 0) + val);
        }

        // sort array
        List<Integer> keys = new ArrayList<>(mp.keySet());
        Collections.sort(keys);

        // result array
        int[][] result = new int[keys.size()][2];
        int idx = 0;
        for (int key : keys) {
            result[idx][0] = key;
            result[idx][1] = mp.get(key);
            idx++;
        }
        
        return result;
    }
}