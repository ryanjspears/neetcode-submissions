from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])

        removals = 0
        previous_end = intervals[0][1]

        for left, right in intervals[1:]:
            # Overlaps with the last interval we kept.
            if left < previous_end:
                removals += 1
            else:
                # Keep this interval.
                previous_end = right

        return removals