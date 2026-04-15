class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        r = 0
        res = 0
        d = {}
        while r < n:
            d[s[r]] = d.get(s[r], 0) + 1
            print(d)
            print(l, r)
            print(s[l:r+1])
            if r - l + 1 - max(d.values()) <= k:
                res = max(res, (r - l + 1))
                r += 1
            else:
                d[s[l]] -= 1
                l += 1
                d[s[r]] -= 1
                r -= 1
                d[s[r]] -= 1
        return res