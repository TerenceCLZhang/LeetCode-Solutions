/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function (flowerbed, n) {
  for (let i = 0; i < flowerbed.length; i++) {
    if (n <= 0) return true;

    const prev_empty = i === 0 || flowerbed[i - 1] === 0;
    const curr_empty = flowerbed[i] === 0;
    const next_empty = i === flowerbed.length - 1 || flowerbed[i + 1] === 0;

    if (prev_empty && curr_empty && next_empty) {
      flowerbed[i] = 1;
      n--;
    }
  }

  return n <= 0;
};

// Time: O(n)
// Space: O(1)
