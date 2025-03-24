class Solution {
    public int countDays(int days, int[][] meetings) {
        // Sort meetings by start time.
        Arrays.sort(meetings, (a, b) -> Integer.compare(a[0], b[0]));
        int ans = 0;
        int end = 0;
        
        // Process each meeting.
        for (int[] meeting : meetings) {
            int st = meeting[0];
            int fin = meeting[1];
            if (st > end) {
                ans += st - end - 1;
            }
            end = Math.max(end, fin);
        }
        
        // If there is a gap after the last meeting.
        if (days > end) {
            ans += days - end;
        }
        
        return ans;
    }
}