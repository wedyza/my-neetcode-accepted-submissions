class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([symbol for symbol in s if symbol.isalpha() or symbol.isdigit()]).lower()
        point = len(s) // 2
        if len(s) % 2 == 0:
            return s[:point] == s[point::][::-1]
        else:
            return s[:point] == s[point + 1:][::-1]