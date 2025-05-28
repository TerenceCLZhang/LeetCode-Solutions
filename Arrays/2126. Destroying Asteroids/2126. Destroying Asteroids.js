/**
 * @param {number} mass
 * @param {number[]} asteroids
 * @return {boolean}
 */
var asteroidsDestroyed = function (mass, asteroids) {
  asteroids.sort((a, b) => a - b);

  for (const a of asteroids) {
    if (a > mass) return false;
    mass += a;
  }

  return true;
};

// Time: O(n log n)
// Space: O(1)
