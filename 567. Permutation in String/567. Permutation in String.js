/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function (s1, s2) {
  const checkArraysEqual = (a1, a2) => {
    for (let i = 0; i < a1.length; i++) {
      if (a1[i] !== a2[i]) {
        return false;
      }
    }
    return true;
  };

  const s1Len = s1.length;
  const s2Len = s2.length;

  if (s1Len > s2Len) {
    return false;
  }

  const s1Count = new Array(26).fill(0);
  const s2Count = new Array(26).fill(0);

  for (let i = 0; i < s1Len; i++) {
    s1Count[s1.charCodeAt(i) - "a".charCodeAt(0)]++;
    s2Count[s2.charCodeAt(i) - "a".charCodeAt(0)]++;
  }

  if (checkArraysEqual(s1Count, s2Count)) {
    return true;
  }

  for (let i = s1Len; i < s2Len; i++) {
    s2Count[s2.charCodeAt(i) - "a".charCodeAt(0)]++;
    s2Count[s2.charCodeAt(i - s1Len) - "a".charCodeAt(0)]--;

    if (checkArraysEqual(s1Count, s2Count)) {
      return true;
    }
  }

  return false;
};
