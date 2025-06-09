class Solution {
    public int findKthNumber(int n, int k) {
        int res = 1;
        k--;

        while(k > 0) {
            int stps = count(n, res, res+ 1);
            if (stps <= k) {
                k -= stps;
                res += 1;
            } else {
                res *= 10;
                k -= 1;
            }
        }

        return res;
    }

    public int count(long n, long a, long b) {
        int sum = 0;
        while (a <= n) {
            sum += (int) (Math.min(n + 1L, b) - a);
            a *= 10;
            b *= 10;
        }

        return sum;
    }
}