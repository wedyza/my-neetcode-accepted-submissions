import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []

        for x, y in points:
            d = x*x + y*y
            heapq.heappush(q, (d, (x, y)))

        largest = [point for d, point in heapq.nsmallest(k, q)]

        return largest