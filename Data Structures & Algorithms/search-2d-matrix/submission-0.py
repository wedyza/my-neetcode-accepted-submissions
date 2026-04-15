class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mega_matrix = []
        for m in matrix:
            mega_matrix.extend(m)
        l = 0
        r = len(mega_matrix) - 1
        while l <= r:
            middle = (l + r) // 2
            if mega_matrix[middle] == target:
                return True
            elif mega_matrix[middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        return False