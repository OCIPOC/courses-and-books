import heapq

data = [7, 8, 2, 1, 4, 5]
heapq.heapify(data)
print(data) # [1, 4, 2, 8, 7, 5]

heapq.heappush(data, 3)
print(data) # [1, 4, 2, 8, 7, 5, 3]

heapq.heappush(data, 0)
print(data) # [[0, 1, 2, 4, 7, 5, 3, 8]

print(heapq.heappop(data)) # 0
print(data) # [1, 4, 2, 8, 7, 5, 3]

print(heapq.heapreplace(data, 10))
print(data)

print(heapq.nlargest(3, data)) # [10, 8, 7]
print(heapq.nsmallest(3, data)) # [2, 3, 4]
