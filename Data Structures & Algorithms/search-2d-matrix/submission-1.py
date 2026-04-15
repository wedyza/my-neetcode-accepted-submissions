class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag = True
        for row in matrix:
            print(row[0], row[-1])
            if row[0] <= target and row[-1] >= target:
                matcher = row
                flag = False
                break
        if flag:
            return False
        l = 0
        r = len(matcher) - 1
        print(matcher)
        while l <= r:
            middle = (l + r) // 2
            if matcher[middle] == target:
                return True
            elif matcher[middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        return False