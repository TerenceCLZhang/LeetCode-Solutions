/**
 * @param {number[]} hours
 * @param {number} target
 * @return {number}
 */
var numberOfEmployeesWhoMetTarget = function (hours, target) {
  let count = 0;
  for (const h of hours) {
    if (h >= target) count++;
  }
  return count;
};

// Time: O(n)
// Space: O(1)
