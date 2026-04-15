class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for symbol in s:
            if symbol in '[{(':
                stack.append(symbol)
            else:
                if len(stack) == 0:
                    return False
                closing_bracket = stack.pop()
                match closing_bracket:
                    case '(':
                        if symbol != ')':
                            return False
                    case '[':
                        if symbol != ']':
                            return False
                    case '{':
                        if symbol != '}':
                            return False
        return len(stack) == 0