/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function (n) {
  let ans = [];
  for (let num = 1; num < n + 1; num++) {
    const div_3 = num % 3;
    const div_5 = num % 5;

    if (div_3 === 0 && div_5 === 0) {
      ans.push("FizzBuzz");
    } else if (div_3 == 0) {
      ans.push("Fizz");
    } else if (div_5 == 0) {
      ans.push("Buzz");
    } else {
      ans.push(num.toString());
    }
  }
  return ans;
};

// Time: O(n)
// Space: O(1)
