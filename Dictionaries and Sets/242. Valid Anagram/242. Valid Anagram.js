/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  if (s.length !== t.length) return false;

  let s_counter = {};
  for (const char of s) {
    if (char in s_counter) s_counter[char]++;
    else s_counter[char] = 1;
  }

  let t_counter = {};
  for (const char of t) {
    if (char in t_counter) t_counter[char]++;
    else t_counter[char] = 1;
  }

  if (s_counter.length !== t_counter.length) return false;

  for (const k in s_counter) {
    if (s_counter[k] !== t_counter[k]) return false;
  }

  return true;
};

// Time: O(n)
// Space O(n)
// Where n is the length of the longest word
