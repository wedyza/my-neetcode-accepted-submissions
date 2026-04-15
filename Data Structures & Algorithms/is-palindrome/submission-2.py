class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([symbol for symbol in s if symbol.isalpha() or symbol.isdigit()]).lower()
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - i - 1]:
                return False
        return True