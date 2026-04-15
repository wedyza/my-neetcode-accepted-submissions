class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 1
        res = 0
        index = 0
        while index + length <= len(s):
            cache = {}
            max_letters = 0
            print(index, length)
            for i in range(index, index + length):
                letters_count = cache.get(s[i], 0) + 1
                cache[s[i]] = letters_count
                max_letters = max(letters_count, max_letters)
            print(cache)
            if len(cache.keys()) == 1 or length - max_letters <= k:
                res = max(res, length)
                length += 1
            else: 
                length = res
                index += 1
        return res