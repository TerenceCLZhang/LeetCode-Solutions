/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
  let ans = [];

  for (let i = 0; i < arr.length; i++) {
    if (Array.isArray(arr[i]) && n > 0) {
      ans.push(...flat(arr[i], n - 1));
    } else {
      ans.push(arr[i]);
    }
  }

  return ans;
};
