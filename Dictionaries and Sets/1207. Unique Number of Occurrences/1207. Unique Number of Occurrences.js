/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function (arr) {
  const counter = {};
  for (const n of arr) {
    counter[n] = (counter[n] || 0) + 1;
  }

  const frequencies = Object.values(counter);
  return frequencies.length === new Set(frequencies).size;
};

// Time: O(n)
// Space: O(n)
