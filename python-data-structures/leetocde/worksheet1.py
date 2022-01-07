from functools import reduce

def merge(intervals: list) -> list:
    intervals.sort()
    start = 1
    while start < len(intervals):
        if intervals[start][0] <= intervals[start - 1][1]:
            end = max(intervals[start][1], intervals[start - 1][1])
            intervals[start - 1][1] = end
            intervals.pop(start)
        else:
            start = start + 1
    
    return intervals

assert merge([[1,4],[4,5]]) == [[1,5]]
assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]