class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        # Sort intervals by ending time
        intervals.sort(key=lambda x: x[1])

        count = 0
        end = intervals[0][1]

        # Check remaining intervals
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                # Overlapping -> remove this interval
                count += 1
            else:
                # Non-overlapping -> keep it
                end = intervals[i][1]

        return count