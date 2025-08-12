/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
  if (numRows === 1) {
    return s;
  }

  const rows = Array.from({ length: numRows }, () => []);
  let pos = 0;
  let dPos = 1;

  for (const c of s) {
    rows[pos].push(c);

    if (pos === numRows - 1) {
      dPos = -1;
    } else if (pos === 0) {
      dPos = 1;
    }

    pos += dPos;
  }

  for (let i = 0; i < numRows; i++) {
    rows[i] = rows[i].join("");
  }

  return rows.join("");
};
