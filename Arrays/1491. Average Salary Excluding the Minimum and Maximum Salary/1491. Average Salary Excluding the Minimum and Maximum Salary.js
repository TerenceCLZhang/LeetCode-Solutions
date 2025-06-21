/**
 * @param {number[]} salary
 * @return {number}
 */
var average = function (salary) {
  const min = Math.min(...salary);
  const max = Math.max(...salary);
  const sum = salary.reduce((a, b) => a + b) - min - max;
  return sum / (salary.length - 2);
};

// Time: O(n)
// Space: O(1)
