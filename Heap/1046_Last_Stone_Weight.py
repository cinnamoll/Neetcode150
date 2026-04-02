class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []
        for s in stones:
            minHeap.append(-s)
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            x = heapq.heappop(minHeap)
            y = heapq.heappop(minHeap)
            if x != y:
                heapq.heappush(minHeap, x - y)
        if len(minHeap) == 1:
            return -minHeap[0]
        return 0