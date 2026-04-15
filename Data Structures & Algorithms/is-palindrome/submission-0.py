class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_string = ''.join([symbol for symbol in s if symbol.isalpha() or symbol.isdigit()]).lower()
        point = len(valid_string) // 2
        if len(valid_string) % 2 == 0:
            return valid_string[:point] == valid_string[point::][::-1]
        else:
            return valid_string[:point] == valid_string[point + 1:][::-1]