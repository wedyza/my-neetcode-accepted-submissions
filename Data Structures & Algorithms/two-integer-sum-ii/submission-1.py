class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for c, i in enumerate(numbers):
            x = target - i
            if x != i and x in numbers:
                index = numbers.index(x) + 1
                if c < index:
                    return [c + 1, index]
                return [index, c + 1]
                