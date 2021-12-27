import heapq

heap = [1, 2, 3, 4]
heapq._heapify_max(heap)
heapq.heappush(heap, 7)
print(heap)

print(heapq._heappop_max(heap))

