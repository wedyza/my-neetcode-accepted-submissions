class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not set(s1) <= set(s2) or len(s1) > len(s2):
            return False
        s2 = s2.lower()
        s1 = s1.lower()
        window = len(s1)
        di = [0] * 26
        for i in s1:
            di[ord(i) - ord('a')] += 1
        d = [0] * 26
        i = 0
        while i + window <= len(s2):
            d = [0] * 26
            for j in range(i, i+window):
                d[ord(s2[j]) - ord('a')] += 1
            print(d)
            if d == di:
                return True
            i += 1
        return False    