class Solution {
    public int maximumCandies(int[] candies, long k) {
        int low = 1;
        int high = 0;

        for (int pile : candies) {
            high = Math.max(high, pile);
        }

        int res = 0;

        while (low <= high) {
            int mid = low + (high - low)/2;
            if (canServe(candies, mid, k)) {
                res = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return res;
    }

    static boolean canServe(int[] candies, int c, long k) {
        long count = 0;
        for (int candy : candies) {
            count += candy/c;
            if (count >= k) {
                return true;
            }
        }

        return count >= k;
    }
}