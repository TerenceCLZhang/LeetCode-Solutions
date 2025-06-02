/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  let ans = [];
  let lMul = 1;
  for (const n of nums) {
    ans.push(lMul);
    lMul *= n;
  }

  let rMul = 1;
  for (let i = nums.length - 1; i > -1; i--) {
    ans[i] *= rMul;
    rMul *= nums[i];
  }

  return ans;
};

// Time: O(n)
// Space: O(1)
