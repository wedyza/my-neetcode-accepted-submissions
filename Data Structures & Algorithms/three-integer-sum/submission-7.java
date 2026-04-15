class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        nums = Arrays.stream(nums).sorted().toArray();
        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            int l = i + 1;
            int r = nums.length - 1;
            while (l < r) {
                int target = nums[i] + nums[l] + nums[r];
                if (target < 0)
                    l += 1;
                else if (target > 0)
                    r -= 1;
                else {
                    res.add(List.of(nums[i], nums[l], nums[r]));
                    l += 1;
                    while (l < r & nums[l] == nums[l-1])
                        l += 1;
                }
            }
        }
        return res;
    }
}
