class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        count = {}
        count2 = {}

        for c in s:
            count[c] = count.get(c, 0) + 1
        
        for c in t:
            count2[c] = count2.get(c, 0) + 1

        return count == count2

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        used = []
        for x in strs:
            anagram = [y for y in strs if self.isAnagram(x, y) and y not in used]
            used.extend(anagram)
            if len(anagram) > 0:
                anagrams.append(anagram)
        
        return anagrams
    