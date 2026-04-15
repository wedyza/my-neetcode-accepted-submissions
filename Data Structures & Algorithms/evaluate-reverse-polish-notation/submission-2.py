class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens = tokens[::-1]
        nums_stack = []
        while len(tokens) > 0:
            token = tokens.pop()
            print(token)
            if token not in ['+', '-', '*', '/']:
                nums_stack.append(token)
            else:
                num1 = int(nums_stack.pop())
                num2 = int(nums_stack.pop())
                match token:
                    case '+':
                        tokens.append(str(num1 + num2))
                    case '-':
                        tokens.append(str(num2 - num1))
                    case '*':
                        tokens.append(str(num2 * num1))
                    case '/':
                        tokens.append(str(int(num2 / num1)))
            print(nums_stack)
        return int(token)