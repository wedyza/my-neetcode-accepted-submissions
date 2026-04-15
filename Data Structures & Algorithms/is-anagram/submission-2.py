class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for sub in s:
            if sub in d1.keys():
                d1[sub] += 1
            else:
                d1[sub] = 1
        
        for sub in t:
            if sub in d2.keys():
                d2[sub] += 1
            else:
                d2[sub] = 1

        if len(d1.keys()) != len(d2.keys()):
            return False

        for i in d1.keys():
            try:
                if d1[i] != d2[i]:
                    return False
            except:
                return False
        
        return True