class Solution {
    public String removeOccurrences(String s, String part) {
        StringBuilder curr = new StringBuilder();
        int n = part.length();
        char en = part.charAt(n - 1);

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            curr.append(ch);

            if (ch == en && curr.length() >= n) {
                String tail = curr.substring(curr.length() - n, curr.length());
                if (tail.equals(part)) {
                    curr.delete(curr.length() - n, curr.length());
                }
            }
        }

        return curr.toString();
    }
}