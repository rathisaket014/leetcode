class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxprof = 0;
        int b = 0;
        int s = 1;

        while (s < prices.size()) {
            if (prices[b] < prices[s]) {
                int prof = prices[s] - prices[b];
                maxprof = std::max(maxprof, prof);
            } else {
                b = s;
            }
            s++;
        }
        return maxprof;
    }
};
