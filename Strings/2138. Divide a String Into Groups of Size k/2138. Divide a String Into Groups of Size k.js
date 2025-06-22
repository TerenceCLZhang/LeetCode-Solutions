/**
 * @param {string} s
 * @param {number} k
 * @param {character} fill
 * @return {string[]}
 */
var divideString = function (s, k, fill) {
  const ans = [];
  let i = 0;

  while (i < s.length) {
    let chunk = s.slice(i, i + k);
    if (chunk.length < k) chunk += fill.repeat(k - chunk.length);
    ans.push(chunk);
    i += k;
  }

  return ans;
};

// Time: O(n)
// Space: O(1)
