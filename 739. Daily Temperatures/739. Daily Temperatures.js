/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function (temperatures) {
  const n = temperatures.length;
  const stack = [];
  const ans = new Array(n).fill(0);

  for (let i = 0; i < n; i++) {
    while (stack.length > 0 && temperatures[i] > temperatures[stack.at(-1)]) {
      const j = stack.pop();
      ans[j] = i - j;
    }
    stack.push(i);
  }

  return ans;
};
