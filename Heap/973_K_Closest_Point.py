class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclid(point: List[int]):
            return math.sqrt(point[0] ** 2 + point[1] ** 2)
        temp = []
        heapq.heapify(temp)
        for point in points:
            heapq.heappush(temp, (-euclid(point), point))
        while len(temp) > k:
            heapq.heappop(temp)
        res = [p for (dist, p) in temp]
        return res