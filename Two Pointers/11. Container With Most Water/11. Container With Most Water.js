/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let l = 0;
  let r = height.length - 1;
  let currMaxArea = 0;

  while (l < r) {
    const minHeight = Math.min(height[l], height[r]);
    const currArea = minHeight * (r - l);
    currMaxArea = Math.max(currMaxArea, currArea);

    if (height[l] < height[r]) l++;
    else r--;
  }

  return currMaxArea;
};

// Time: O(n)
// Space: O(1)
