import java.util.*;

class Solution {
    public int maxDifference(String s) {
        HashMap<Character, Integer> freq = new HashMap<>();

        for (char ch : s.toCharArray()) {
            freq.put(ch, freq.getOrDefault(ch, 0) + 1);
        }

        List<Integer> oddFreqs = new ArrayList<>();
        List<Integer> evenFreqs = new ArrayList<>();

        for (int f : freq.values()) {
            if (f % 2 == 0) {
                evenFreqs.add(f);
            } else {
                oddFreqs.add(f);
            }
        }

        int maxDiff = Integer.MIN_VALUE;

        for (int odd : oddFreqs) {
            for (int even : evenFreqs) {
                maxDiff = Math.max(maxDiff, odd - even);
            }
        }

        return maxDiff;
    }
}
