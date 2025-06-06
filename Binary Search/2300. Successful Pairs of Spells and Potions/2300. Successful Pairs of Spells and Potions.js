/**
 * @param {number[]} spells
 * @param {number[]} potions
 * @param {number} success
 * @return {number[]}
 */
var successfulPairs = function (spells, potions, success) {
  potions.sort((a, b) => a - b);
  let ans = [];

  for (const s of spells) {
    let low = 0;
    let high = potions.length - 1;
    let index = potions.length;

    while (low <= high) {
      const mid = Math.floor((low + high) / 2);
      if (s * potions[mid] >= success) {
        index = mid;
        high = mid - 1;
      } else low = mid + 1;
    }

    ans.push(potions.length - index);
  }

  return ans;
};

// Time: O(m log m + n log m)
// Space: O(1)
