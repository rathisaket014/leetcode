class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> res = new ArrayList<>();

        int curr = 1;

        for(int i = 0; i < n; i++) {
            res.add(curr);
            if (curr * 10 > n) {
                if (curr == n) {
                    curr = curr / 10;
                }
                curr++;
                while (curr % 10 == 0) {
                    curr = curr / 10;
                }
            } else {
                curr *= 10;
            }
        }

        return res;
    }
}