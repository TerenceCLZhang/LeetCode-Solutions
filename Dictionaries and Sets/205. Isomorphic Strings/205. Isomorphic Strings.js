/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function (s, t) {
  if (s.length !== t.length) return false;

  map1 = new Map();
  map2 = new Map();

  for (let i = 0; i < s.length; i++) {
    const char_s = s[i];
    const char_t = t[i];

    if (map1.has(char_s)) {
      if (map1.get(char_s) !== char_t) return false;
    } else {
      map1.set(char_s, char_t);
    }

    if (map2.has(char_t)) {
      if (map2.get(char_t) !== char_s) return false;
    } else {
      map2.set(char_t, char_s);
    }
  }

  return true;
};

// Time: O(n)
// Space: O(n)
