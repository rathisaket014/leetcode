class Solution {
    public boolean check(String sub, String s, int k) {
        int cnt = 0, i = 0;
        for (char c : s.toCharArray()) {
            if (i < sub.length() && c == sub.charAt(i)) {
                i++;
                if (i == sub.length()) {
                    i = 0;
                    cnt++;
                    if (cnt == k) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public String longestSubsequenceRepeatedK(String s, int k) {
        Map<Character, Integer> frq = new HashMap<>();
        for (char c : s.toCharArray()) {
            frq.put(c, frq.getOrDefault(c, 0) + 1);
        }

        List<Character> isValid = new ArrayList<>();
        for (char c = 'z'; c >= 'a'; c--) {
            if (frq.getOrDefault(c, 0) >= k) {
                isValid.add(c);
            }
        }

        int mx = s.length() / k;
        String res = "";
        Queue<String> q = new LinkedList<>();
        q.offer("");
        while (!q.isEmpty()) {
            String curr = q.poll();
            for (char c : isValid) {
                String next = curr + c;
                if (next.length() > mx)
                    continue;
                if (check(next, s, k)) {
                    if (next.length() > res.length() ||
                        (next.length() == res.length() && next.compareTo(res) > 0)) {
                        res = next;
                    }
                    q.offer(next);
                }
            }
        }
        return res;
    }
}