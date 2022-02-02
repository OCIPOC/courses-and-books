import heapq

def min_rooms(intervals: list):
    intervals.sort(key=lambda x: x[0])
    heap = []
    min_rooms = 0

    for i in intervals:
        while heap and heapq.nsmallest(1, heap)[0] <= i[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, i[1])

        if len(heap) > min_rooms:
            min_rooms = len(heap)
    
    return min_rooms

assert min_rooms([[0,30],[5,10],[15,20]]) == 2
assert min_rooms([[7,10],[2,4]]) == 1
assert min_rooms([[13,15],[1,13]]) == 1