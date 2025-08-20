/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function (piles, h) {
  let low = 1;
  let high = Math.max(...piles);

  while (low < high) {
    mid = Math.floor((low + high) / 2);

    let hours = 0;
    for (const pile of piles) {
      hours += Math.floor(pile / mid);
      if (pile % mid !== 0) {
        hours++;
      }
    }

    if (hours <= h) {
      high = mid;
    } else {
      low = mid + 1;
    }
  }

  return low;
};
