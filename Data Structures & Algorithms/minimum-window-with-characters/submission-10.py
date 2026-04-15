from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        d = Counter(t)
        b = {}
        symbols_we_looking = d.keys()
        for symbol in symbols_we_looking:
            b[symbol] = 0
        matches = 0
        matches_we_need = len(symbols_we_looking)
        l = 0
        r = 0
        win = (-1, -1)
        while r < len(s):
            if s[r] in symbols_we_looking:
                b[s[r]] += 1
                if b[s[r]] == d[s[r]]:
                    matches += 1
                    if matches == matches_we_need:
                        while matches == matches_we_need:
                            if win[0] == -1 or win[1] - win[0] >= r - l:
                                win = (l, r)
                            if s[l] in symbols_we_looking:
                                b[s[l]] -= 1
                                if b[s[l]] < d[s[l]]:
                                    matches -= 1
                            l += 1
                            
            r += 1
        if win == (-1, -1):
            return ''
        return s[win[0]:win[1]+1]