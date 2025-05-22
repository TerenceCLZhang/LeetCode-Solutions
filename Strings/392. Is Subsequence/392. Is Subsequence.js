/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function (s, t) {
  if (!s) return true;
  if (s.length > t.length) return false;

  let s_idx = 0;
  let t_idx = 0;

  while (t_idx < t.length) {
    if (s[s_idx] === t[t_idx]) {
      s_idx++;
      if (s_idx === s.length) return true;
    }
    t_idx++;
  }

  return false;
};

// Time: O(n)
// Space: O(1)
