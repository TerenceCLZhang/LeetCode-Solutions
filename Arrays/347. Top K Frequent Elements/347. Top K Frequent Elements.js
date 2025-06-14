/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  let counter = {};
  for (const n of nums) {
    counter[n] = (counter[n] || 0) + 1;
  }

  let arr = new Array(nums.length + 1).fill(0);
  for (const [num, freq] of Object.entries(counter)) {
    if (arr[freq] === 0) arr[freq] = [Number(num)];
    else arr[freq].push(Number(num));
  }

  let ans = [];
  for (let i = nums.length; i > 0; i--) {
    if (arr[i] !== 0) ans.push(...arr[i]);
    if (ans.length >= k) break;
  }

  return ans;
};

// Time: O(n)
// Space: O(n)
