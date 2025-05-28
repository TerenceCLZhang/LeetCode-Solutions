/**
 * @param {string} s
 * @return {boolean}
 */
var areNumbersAscending = function (s) {
  let num = 0;
  let curr_num = "";

  for (const char of s) {
    if (char >= "0" && char <= "9") curr_num += char;
    else {
      if (curr_num !== "") {
        if (Number(curr_num) <= num) return false;
        num = Number(curr_num);
        curr_num = "";
      }
    }
  }

  if (curr_num !== "") {
    if (Number(curr_num) <= num) return false;
    num = Number(curr_num);
  }

  return num;
};

// Time: O(n)
// Space: O(1)
