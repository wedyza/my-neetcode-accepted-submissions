class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag = True
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            middle = (top + bottom) // 2
            if matrix[middle][-1] < target:
                top = middle + 1
            else:
                bottom = middle - 1
        if top >= len(matrix):
            return False
        matcher = matrix[top]
        l = 0
        r = len(matcher) - 1
        while l <= r:
            middle = (l + r) // 2
            if matcher[middle] == target:
                return True
            elif matcher[middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        return False