/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function (candies, extraCandies) {
  let ans = [];
  const maxx = Math.max(...candies);
  for (const c of candies) {
    const extra = c + extraCandies;
    if (extra >= maxx) ans.push(true);
    else ans.push(false);
  }
  return ans;
};

// Time: O(n)
// Space: O(1)
