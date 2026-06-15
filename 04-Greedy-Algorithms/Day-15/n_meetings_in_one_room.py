class Solution:
    def maximumMeetings(self, n: int, start: list[int], end: list[int]) -> int:
        meetings = [(start[i], end[i]) for i in range(n)]
        meetings.sort(key=lambda x: x[1])
        
        count = 1
        last_end_time = meetings[0][1]
        
        for i in range(1, n):
            if meetings[i][0] > last_end_time:
                count += 1
                last_end_time = meetings[i][1]
                
        return count
