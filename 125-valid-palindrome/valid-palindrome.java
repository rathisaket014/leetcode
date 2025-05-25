class Solution {
    public boolean isPalindrome(String s) {
        int lft = 0;
        int rgt = s.length() - 1;

        while (lft < rgt) {
            while (lft < rgt && !Character.isLetterOrDigit(s.charAt(lft))) {
                lft++;
            }

            while (lft < rgt && !Character.isLetterOrDigit(s.charAt(rgt))) {
                rgt--;
            }

            if (Character.toLowerCase(s.charAt(lft)) != Character.toLowerCase(s.charAt(rgt))) {
                return false;
            }

            lft++;
            rgt--;
        }

        return true;
    }
}