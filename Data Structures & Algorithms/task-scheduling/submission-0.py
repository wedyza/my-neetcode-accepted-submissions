class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}

        for task in tasks:
            d[task] = d.get(task, 0) - 1
        
        h = [cnt for cnt in d.values()]
        heapq.heapify(h)
        time = 0
        q = deque()
        print(h)
        while q or h:
            time += 1

            if not h:
                time = q[0][1]
            else:
                o = 1 + heapq.heappop(h)
                if o:
                    q.append([o, time + n])
            if q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])
        return time