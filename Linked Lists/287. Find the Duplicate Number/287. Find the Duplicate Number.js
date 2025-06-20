/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function (nums) {
  let fast = 0,
    slow = 0;

  while (true) {
    fast = nums[nums[fast]];
    slow = nums[slow];

    if (fast === slow) break;
  }

  slow = 0;
  while (fast !== slow) {
    fast = nums[fast];
    slow = nums[slow];
  }

  return slow;
};

// Time: O(n)
// Space: O(1)
