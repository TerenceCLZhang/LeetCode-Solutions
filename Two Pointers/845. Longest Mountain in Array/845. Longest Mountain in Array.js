/**
 * @param {number[]} arr
 * @return {number}
 */
var longestMountain = function (arr) {
  let longest = 0;
  let i = 0;
  while (i < arr.length - 1) {
    if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
      let l = i - 1;
      let r = i + 1;

      while (l > 0 && arr[l] > arr[l - 1]) l--;
      while (r < arr.length - 1 && arr[r] > arr[r + 1]) r++;

      longest = Math.max(longest, r - l + 1);
      i = r;
    } else {
      i++;
    }
  }
  return longest;
};

// Time: O(n)
// Space: O(1)
