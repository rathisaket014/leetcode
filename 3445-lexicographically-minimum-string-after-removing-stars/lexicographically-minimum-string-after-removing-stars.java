class Solution {
    public String clearStars(String s) {
        PriorityQueue<Character> pq = new PriorityQueue<>();
        List<List<Integer>> alpha = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            alpha.add(new ArrayList<>());
        }

        char ch;
        char[] sArray = s.toCharArray();
        for (int i = 0; i < s.length(); i++) {
            if (sArray[i] == '*') {
                ch = pq.peek();
                sArray[alpha.get(ch - 'a').get(alpha.get(ch - 'a').size() - 1)] = '*';
                alpha.get(ch - 'a').remove(alpha.get(ch - 'a').size() - 1);
                if (alpha.get(ch - 'a').isEmpty()) {
                    pq.poll();
                }
                continue;
            }

            if (alpha.get(sArray[i] - 'a').isEmpty()) {
                pq.add(sArray[i]);
            }
            alpha.get(sArray[i] - 'a').add(i);
        }

        StringBuilder res = new StringBuilder();
        for (char c : sArray) {
            if (c >= 'a') {
                res.append(c);
            }
        }

        return res.toString();
    }
}
