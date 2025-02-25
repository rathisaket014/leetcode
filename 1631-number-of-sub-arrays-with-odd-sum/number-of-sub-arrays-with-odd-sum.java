class Solution {
    public int numOfSubarrays(int[] arr) {
        int mod = 1_000_000_007;
        long oddCount = 0;
        long evenCount = 1;
        long prefixSum = 0;
        long ans = 0;

        for(int num : arr) {
            prefixSum += num;
            
            if(prefixSum % 2 == 0) {
                ans = (ans + oddCount) % mod;
                evenCount++;
            } else {
                ans = (ans + evenCount) % mod;
                oddCount++;
            }
        }

        return (int) ans;
    }
}