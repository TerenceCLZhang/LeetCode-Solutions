/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function (a, b) {
  a = BigInt("0b" + a);
  b = BigInt("0b" + b);

  while (b) {
    const without_carry = a ^ b;
    const with_carry = (a & b) << 1n;
    a = without_carry;
    b = with_carry;
  }

  return a.toString(2);
};
