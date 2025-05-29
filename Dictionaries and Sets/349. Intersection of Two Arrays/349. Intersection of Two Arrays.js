/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function (nums1, nums2) {
  let small, large;
  if (nums1.length < nums2.length) {
    [small, large] = [nums1, nums2];
  } else {
    [small, large] = [nums2, nums1];
  }

  sett = new Set(small);
  ans = [];
  for (const n of large) {
    if (sett.has(n)) {
      ans.push(n);
      sett.delete(n);
    }
  }

  return ans;
};

// Time: O(n + m)
// Space: O(min(n, m))
// Where n is the length of nums1 and m is the length of nums2
