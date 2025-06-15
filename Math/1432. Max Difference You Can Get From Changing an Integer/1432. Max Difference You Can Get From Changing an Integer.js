/**
 * @param {number} num
 * @return {number}
 */
var maxDiff = function (num) {
  const num_str = num.toString();
  let maxx, minn;

  let max_flag = false;
  for (const char of num_str) {
    if (char !== "9") {
      maxx = num_str.replaceAll(char, "9");
      max_flag = true;
      break;
    }
  }
  if (!max_flag) maxx = num_str;

  if (num_str[0] != "1") {
    minn = num_str.replaceAll(num_str[0], "1");
  } else {
    let min_flag = false;
    for (const char of num_str.slice(1)) {
      if (!"01".includes(char)) {
        minn = num_str.replaceAll(char, "0");
        min_flag = true;
        break;
      }
    }
    if (!min_flag) minn = num_str;
  }

  return Number(maxx) - Number(minn);
};

// Time: O(l)
// Space: O(l)
// Where l is the number of digits in n