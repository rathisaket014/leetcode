class Solution {
    public int strStr(String haystack, String needle) {
        int n = needle.length();
        int m = haystack.length();

        for (int i = 0, j = n; j <= m; i++, j++) {
            if (haystack.substring(i, j).equals(needle)) {
                return i;
            }
        }

        return -1;
    }
}