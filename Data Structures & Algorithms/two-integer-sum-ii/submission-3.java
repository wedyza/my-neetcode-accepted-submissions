class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int leftPointer = 0;
        int rightPointer = numbers.length - 1;

        while (true){
            if (numbers[leftPointer] + numbers[rightPointer] > target)
                rightPointer -= 1;
            else if (numbers[leftPointer] + numbers[rightPointer] < target)
                leftPointer += 1;
            else
                return new int[]{leftPointer + 1, rightPointer + 1};
        }
    }
}