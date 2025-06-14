/**
 * @param {number} num
 * @return {number}
 */
var minMaxDifference = function (num) {
  let maxx = num.toString();
  let minn = num.toString();

  let i = 0;
  while (i < maxx.length && maxx[i] === "9") i++;

  if (i < maxx.length) maxx = maxx.replaceAll(maxx[i], "9");
  minn = minn.replaceAll(minn[0], "0");

  return Number(maxx) - Number(minn);
};

// Time: O(n)
// Space: O(1)
