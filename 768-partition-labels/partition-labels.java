class Solution {
    public List<Integer> partitionLabels(String s) {
        int[] Idx = new int[26];
        for (int i = 0; i < s.length(); i++) {
            Idx[s.charAt(i) - 'a'] = i; // to convert ch ascii to 0 - 25 range
        }

        List<Integer> res = new ArrayList<>();
        int st = 0;
        int en = 0;

        for (int i = 0; i < s.length(); i++) {
            st++;

            en = Math.max(en, Idx[s.charAt(i) - 'a']);

            if (i == en) {
                res.add(st);
                st = 0;  // Reset st for the next partition.
            }
        }

        return res;
    }
}