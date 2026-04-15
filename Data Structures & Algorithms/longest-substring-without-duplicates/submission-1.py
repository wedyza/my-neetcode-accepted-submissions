class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        s = list(s)
        length = 1
        index = 0
        while index + length < len(s):
            substring = s[index:index + length + 1]
            if len(set(substring)) == len(substring):
                length += 1
            else:
                index += 1
        return length