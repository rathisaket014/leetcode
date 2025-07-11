class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> fq;

        for (int num : nums) {
            fq[num]++;
        }

        for (auto& entry : fq) {
            if (entry.second > nums.size() / 2) {
                return entry.first;
            }
        }

        return -1;
    }
};