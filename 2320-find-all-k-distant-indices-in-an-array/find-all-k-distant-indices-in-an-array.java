class Solution {

    public List<Integer> findKDistantIndices(int[] nums, int key, int k) {
        int n = nums.length;
        
        List<Integer> ans = new ArrayList<>();
        
        
        int i = 0; 
        
        for (int j = 0; j < n; ++j) {
            if (nums[j] == key) {
                int l = Math.max(i, j - k);
                
                i = Math.min(n - 1, j + k) + 1;
                
                for (int o = l; o < i; ++o) {
                    ans.add(o);
                }
            }
        }
        return ans;
    }
}