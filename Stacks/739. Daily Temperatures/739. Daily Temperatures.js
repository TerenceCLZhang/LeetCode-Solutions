/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function (temperatures) {
  let stack = [];
  const ans = new Array(temperatures.length).fill(0);

  for (let i = 0; i < temperatures.length; i++) {
    while (stack && temperatures[stack[stack.length - 1]] < temperatures[i]) {
      j = stack.pop();
      ans[j] = i - j;
    }
    stack.push(i);
  }

  return ans;
};

// Time: O(n)
// Space: O(n)
