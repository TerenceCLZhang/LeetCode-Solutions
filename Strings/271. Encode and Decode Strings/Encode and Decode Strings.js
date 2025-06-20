class Solution {
  /**
   * @param {string[]} strs
   * @returns {string}
   */
  encode(strs) {
    let encoded_string = [];
    for (const s of strs) {
      encoded_string.push(`${s.length}#${s}`);
    }
    return encoded_string.join("");
  }

  /**
   * @param {string} str
   * @returns {string[]}
   */
  decode(str) {
    const ans = [];
    let i = 0;

    while (i < str.length) {
      let j = i;
      while (str[j] !== "#") j++;
      const length = Number(str.slice(i, j));
      ans.push(str.slice(j + 1, j + 1 + length));
      i = j + 1 + length;
    }

    return ans;
  }
}

// Time: O(k)
// Space: O(k)
// Where k is the number of characters
