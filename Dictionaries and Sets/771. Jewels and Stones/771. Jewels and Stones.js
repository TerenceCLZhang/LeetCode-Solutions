/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function (jewels, stones) {
  const j = new Set(jewels);
  let c = 0;
  for (let s of stones) {
    if (j.has(s)) {
      c++;
    }
  }
  return c;
};

// Time: O(n + m)
// Space: O(m)
