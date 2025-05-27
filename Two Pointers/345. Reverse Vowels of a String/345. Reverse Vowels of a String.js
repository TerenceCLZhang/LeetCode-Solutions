/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function (s) {
  const vowels = new Set("aeiouAEIOU");
  let l = 0;
  let r = s.length - 1;
  s = s.split("");

  while (l < r) {
    if (!vowels.has(s[l])) {
      l++;
      continue;
    }

    if (!vowels.has(s[r])) {
      r--;
      continue;
    }

    [s[l], s[r]] = [s[r], s[l]];
    l++;
    r--;
  }

  return s.join("");
};

// Time: O(n)
// Space: O(n)
