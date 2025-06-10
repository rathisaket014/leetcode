import java.util.*;

class Solution {
    public int maxDifference(String s) {
        HashMap<Character, Integer> freq = new HashMap<>();

        // Count frequencies
        for (char ch : s.toCharArray()) {
            freq.put(ch, freq.getOrDefault(ch, 0) + 1);
        }

        List<Integer> oddFreqs = new ArrayList<>();
        List<Integer> evenFreqs = new ArrayList<>();

        // Separate into odd and even
        for (int f : freq.values()) {
            if (f % 2 == 0) {
                evenFreqs.add(f);
            } else {
                oddFreqs.add(f);
            }
        }

        int maxDiff = Integer.MIN_VALUE;

        // Try all (odd - even) combinations
        for (int odd : oddFreqs) {
            for (int even : evenFreqs) {
                maxDiff = Math.max(maxDiff, odd - even);
            }
        }

        return maxDiff;
    }
}
