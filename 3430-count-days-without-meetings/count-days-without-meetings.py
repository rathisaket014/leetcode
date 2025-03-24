class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x : x[0])
        ans = 0
        end = 0

        for st, fin in meetings:
            if st > end:
                ans += st - end - 1
            end = max(end, fin)
        
        if days > end:
            ans += days - end
        
        return ans