/**
 * @param {number} num
 * @return {number}
 */
var countEven = function (num) {
  const checkEvenSum = (num) => {
    let summ = 0;
    while (num > 0) {
      summ += num % 10;
      num = Math.floor(num / 10);
    }
    return summ % 2 === 0;
  };

  let count = 0;
  for (let i = 1; i <= num; i++) {
    if (checkEvenSum(i)) count++;
  }

  return count;
};


// Time: O(n log n)
// Space: O(1)