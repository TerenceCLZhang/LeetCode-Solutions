/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function (nums) {
  const n = nums.length;
  const ans = [];
  const curr = [];

  const backtrack = (i) => {
    if (i === n) {
      ans.push([...curr]);
      return;
    }

    backtrack(i + 1);

    curr.push(nums[i]);
    backtrack(i + 1);
    curr.pop();
  };

  backtrack(0);
  return ans;
};
