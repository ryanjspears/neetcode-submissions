from typing import List


class Solution:
    def insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int]
    ) -> List[List[int]]:
        result = []
        left, right = newInterval

        for interval_left, interval_right in intervals:
            # Current interval is completely before the new interval.
            if interval_right < left:
                result.append([interval_left, interval_right])

            # Current interval is completely after the new interval.
            elif interval_left > right:
                result.append([left, right])
                left, right = interval_left, interval_right

            # The intervals overlap, so combine them.
            else:
                left = min(left, interval_left)
                right = max(right, interval_right)

        result.append([left, right])

        return result