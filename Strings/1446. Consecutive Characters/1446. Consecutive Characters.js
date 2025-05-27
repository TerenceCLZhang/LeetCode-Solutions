/**
 * @param {string} s
 * @return {number}
 */
var maxPower = function (s) {
  let max_power = 1;
  let curr_power = 1;

  for (let i = 1; i < s.length; i++) {
    if (s[i] == s[i - 1]) curr_power++;
    else {
      max_power = Math.max(max_power, curr_power);
      curr_power = 1;
    }
  }

  return Math.max(max_power, curr_power);
};

// Time: O(n)
// Space: O(1)
