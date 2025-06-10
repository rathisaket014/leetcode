class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int buy = 0;
        int sell = 1;

        while (sell < prices.length) {
            if (prices[buy] < prices[sell]) {
                int prof = prices[sell] - prices[buy];
                max = Math.max(max, prof);
            } else {
                buy = sell;
            }
            sell++;
        }

        return max;
    }
}