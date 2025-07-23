class Solution {
    public boolean validPalindrome(String s) {
        int st = 0, en = s.length() - 1;

        while (st < en) {
            if (s.charAt(st) == s.charAt(en)) {
                st++;
                en--;
            } else {
                return isPalindrome(s, st + 1, en) || isPalindrome(s, st, en - 1);
            }
        }
        return true;
    }

    private boolean isPalindrome(String s, int st, int en) {
        while (st < en) {
            if (s.charAt(st++) != s.charAt(en--)) return false;
        }
        return true;
    }
}
