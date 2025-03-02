class Solution {
    public int[][] mergeArrays(int[][] nums1, int[][] nums2) {
        // Map<Integer, Integer> mp = new HashMap<>();
        
        // // for first array
        // for (int[] i : nums1) {
        //     int id = i[0];
        //     int val = i[1];
        //     mp.put(id, mp.getOrDefault(id, 0) + val);
        // }

        // // for second array
        // for (int[] j : nums2) {
        //     int id = j[0];
        //     int val = j[1];
        //     mp.put(id, mp.getOrDefault(id, 0) + val);
        // }

        // // sort array
        // List<Integer> keys = new ArrayList<>(mp.keySet());
        // Collections.sort(keys);

        // // result array
        // int[][] result = new int[keys.size()][2];
        // int idx = 0;
        // for (int key : keys) {
        //     result[idx][0] = key;
        //     result[idx][1] = mp.get(key);
        //     idx++;
        // }
        
        // return result;

        List<int[]> ml = new ArrayList<>();
        int i = 0, j = 0;

        // merge two arrays
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i][0] == nums2[j][0]) {
                ml.add(new int[] { nums1[i][0], nums1[i][1] + nums2[j][1] });
                i++;
                j++;
            } else if (nums1[i][0] < nums2[j][0]) {
                ml.add(new int[] { nums1[i][0], nums1[i][1] });
                i++;
            } else {
                ml.add(new int[] { nums2[j][0], nums2[j][1] });
                j++;
            }
        }

        while(i < nums1.length) {
            ml.add(new int[] { nums1[i][0], nums1[i][1] });
            i++;
        }

        while(j < nums2.length) {
            ml.add(new int[] { nums2[j][0], nums2[j][1] });
            j++;
        }

        int[][] res = new int[ml.size()][2];
        for (int k = 0; k < ml.size(); k++) {
            res[k] = ml.get(k);
        }

        return res;
    }
}