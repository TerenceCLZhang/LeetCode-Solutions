/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function (nums) {
  const n = nums.length;
  const ans = [];
  const curr = [];
  const used = new Array(n).fill(false);

  const backtrack = () => {
    if (curr.length === n) {
      ans.push([...curr]);
      return;
    }

    for (let i = 0; i < n; i++) {
      if (!used[i]) {
        curr.push(nums[i]);
        used[i] = true;
        backtrack();
        curr.pop();
        used[i] = false;
      }
    }
  };

  backtrack();
  return ans;
};
