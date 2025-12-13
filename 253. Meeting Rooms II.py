"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        max_days = 0
        days = 0

        s = e = 0
        while s < n:
            if starts[s] < ends[e]:
                days += 1
                s += 1
            else:
                days -= 1
                e += 1
            max_days = max(max_days, days)

        return max_days
