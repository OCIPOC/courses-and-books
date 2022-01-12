import heapq

class StockPrice:    
    def __init__(self):
        self.prices = {}
        self.min_heap = []
        self.max_heap = []
        self.last_ts = None
        
    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        if not self.last_ts or  self.last_ts < timestamp:
            self.last_ts = timestamp

        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))
        
          
    def current(self) -> int:
        return self.prices[self.last_ts]

    def maximum(self) -> int:
        while self.max_heap[0][0] != self.prices[self.max_heap[0][1]]: 
            heapq.heappop(self.max_heap)
        return self.max_heap[0][0]

    def minimum(self) -> int:
        while self.min_heap[0][0] != self.prices[self.min_heap[0][1]]: 
            heapq.heappop(self.min_heap)
        return self.min_heap[0][0]
        
