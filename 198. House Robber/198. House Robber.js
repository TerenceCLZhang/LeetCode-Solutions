/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  const n = nums.length;
  if (n == 1) {
    return nums[0];
  }

  let rob1 = nums[0];
  let rob2 = Math.max(rob1, nums[1]);

  for (let i = 2; i < n; i++) {
    [rob1, rob2] = [rob2, Math.max(rob2, rob1 + nums[i])];
  }

  return rob2;
};
