class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = 0;
        int lastIndex = matrix[0].length - 1;
        if (lastIndex == -1)
            return false;
        System.out.println(lastIndex);
        while (row < matrix.length && matrix[row][lastIndex] < target){
            row += 1;
        }
        if (row == matrix.length)
            return false;
        int l = 0;
        int r = lastIndex;
        while (l <= r){
            int middle = (l + r) / 2;
            if (matrix[row][middle] == target)
                return true;
            else if (matrix[row][middle] < target)
                l = middle + 1;
            else
                r = middle - 1;
        }
        return false;
    }
}
