class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 1;
        int maxprice = 0;

        while (r < prices.length){
            if (prices[l] < prices[r])
                maxprice = Math.max(maxprice, prices[r] - prices[l]);
            else
                l = r;
            r += 1;
        }
        return maxprice;
    }
}
