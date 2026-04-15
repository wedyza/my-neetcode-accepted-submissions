class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag = True
        row = 0
        while row < len(matrix) and matrix[row][-1] < target:
            row += 1
        if row == len(matrix):
            return False
        matcher = matrix[row]
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