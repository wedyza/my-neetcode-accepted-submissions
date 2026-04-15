class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures = temperatures[::-1]
        res = [0]
        stack = [temperatures.pop()]
        while len(temperatures) > 0:
            value = temperatures.pop()
            print(res[-1])
            print(value, stack[-1])
            if value == stack[-1]:
                if res[-1] != 0:
                    res.append(res[-1] + 1)
                else:
                    res.append(0)
            elif value < stack[-1]:
                res.append(1)
            else:
                b4 = len(res)
                i = len(stack) - 2
                c = 1
                while i >= 0:
                    another_value = stack[i]
                    if value == another_value:
                        if res[-1 - c] != 0:
                            res.append(res[-1 - c] + c + 1)
                        else:
                            res.append(0)
                        break
                    elif value < another_value:
                        res.append(1 + c)
                        break
                    c += 1
                    i -= 1
                if len(res) == b4:
                    res.append(0)
            stack.append(value)
        return res[::-1]