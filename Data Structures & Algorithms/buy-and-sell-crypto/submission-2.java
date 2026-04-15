class Solution {
    public int maxProfit(int[] prices) {
        int price = 0;
        int minPrice = prices[0];
        for (int p : prices){
            price = Math.max(price, p - minPrice);
            minPrice = Math.min(minPrice, p);
        }
        return price;
    }
}
