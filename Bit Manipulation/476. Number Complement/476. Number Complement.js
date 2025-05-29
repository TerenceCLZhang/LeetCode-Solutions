/**
 * @param {number} num
 * @return {number}
 */
var findComplement = function (num) {
  const num_bits = num.toString(2).length;
  const max_num = 2 ** num_bits - 1;
  return num ^ max_num;
};

// Time: O(1)
// Space: O(1)
