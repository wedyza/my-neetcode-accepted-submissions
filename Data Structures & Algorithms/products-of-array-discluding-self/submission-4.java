class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] prefix = new int[n];
        int[] suffix =  new int[n];
        prefix[0] = 1;
        suffix[n-1] = 1;
        int m = 1;

        for (int i = 0; i < n; i++){
            if (i > 0)
                prefix[i] = m;
            m *= nums[i];
        }
        m = 1;
        for (int i = n-1; i > -1; i--){
            if (i != n-1)
                suffix[i] = m;
            m *= nums[i];
        }

        int[] answer = new int[n];
        for (int i = 0; i < n; i++)
            answer[i] =  prefix[i] * suffix[i];

        return answer;
    }
}