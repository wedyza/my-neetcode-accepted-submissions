class Solution {
    public int maxArea(int[] heights) {
        int res = -1;
        int l = 0;
        int r = heights.length - 1;
        while (l < r){
            int target = (r - l) * Math.min(heights[l], heights[r]);
            res = Math.max(res, target);
            if (heights[l] < heights[r])
                l += 1;
            else
                r -= 1;
        }
        return res;
    }
}
