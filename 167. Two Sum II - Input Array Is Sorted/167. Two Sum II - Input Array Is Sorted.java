class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;

        while (left < right) {
            int summ = numbers[left] + numbers[right];
            if (summ == target) {
                return new int[] {left + 1, right + 1};
            } else if (summ > target) {
                right--;
            } else {
                left++;
            }
        }

        throw new Error("No solution");
    }
}