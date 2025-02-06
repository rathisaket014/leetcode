class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        if (s1.equals(s2)) {
            return true;
        }
        
        // Use a list to store indices where s1 and s2 differ.
        int[] diff = new int[2];
        int diffCount = 0;
        
        // Loop over the characters of the strings.
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                // If more than 2 differences, return false.
                if (diffCount == 2) {
                    return false;
                }
                diff[diffCount] = i;
                diffCount++;
            }
        }
        
        // If the number of differences is not exactly 2, return false.
        if (diffCount != 2) {
            return false;
        }
        
        // Check if swapping the two differing indices in one of the strings would result in equality.
        return s1.charAt(diff[0]) == s2.charAt(diff[1]) && s1.charAt(diff[1]) == s2.charAt(diff[0]);
    }
}