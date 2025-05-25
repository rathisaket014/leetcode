class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int st = 0;
        int en = numbers.length - 1;

        while (st < en) {
            int sum = numbers[st] + numbers[en];

            if (sum > target) {
                en--;
            }
            if (sum < target) {
                st++;
            }

            if (sum == target) {
                return new int[] {st + 1, en + 1};
            }
        }

        return new int[] {-1, -1};
    }
}