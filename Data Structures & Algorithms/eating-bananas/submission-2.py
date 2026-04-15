class Solution:
    def count_hours(self, piles, k):
        return sum([math.ceil(i / k) for i in piles])

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if h == n:
            return max(piles)
        r = max(piles)
        l = 1
        res = r
        while l <= r:
            middle = (r + l) // 2
            hours = self.count_hours(piles, middle)
            print(hours, middle)
            if hours <= h:
                res = middle
                r = middle - 1
            else:
                l = middle + 1
        return res