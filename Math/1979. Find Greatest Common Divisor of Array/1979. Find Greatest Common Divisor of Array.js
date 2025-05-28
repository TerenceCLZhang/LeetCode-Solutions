/**
 * @param {number[]} nums
 * @return {number}
 */
var findGCD = function (nums) {
  const gcd = (a, b) => {
    while (b) {
      [a, b] = [b, a % b];
    }
    return a;
  };

  const minn = Math.min(...nums);
  const maxx = Math.max(...nums);

  return gcd(minn, maxx);
};

// Time: O(n)
// Space: O(1)
