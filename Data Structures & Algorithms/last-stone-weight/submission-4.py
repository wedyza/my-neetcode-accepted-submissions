import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            q1 = -(heapq.heappop(stones))
            q2 = -(heapq.heappop(stones))
            if q1 == q2:
                continue
            else:
                m = abs(q1 - q2)
                heapq.heappush(stones, -m)
        if len(stones) == 0:
            return 0
        return -stones[0]