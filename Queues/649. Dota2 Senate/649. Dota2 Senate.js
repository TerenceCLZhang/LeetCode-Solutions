/**
 * @param {string} senate
 * @return {string}
 */
var predictPartyVictory = function (senate) {
  let r_queue = [];
  let d_queue = [];

  for (let i = 0; i < senate.length; i++) {
    if (senate[i] == "R") r_queue.push(i);
    else d_queue.push(i);
  }

  while (r_queue.length > 0 && d_queue.length > 0) {
    const r = r_queue.shift();
    const d = d_queue.shift();
    if (r < d) r_queue.push(r + senate.length);
    else d_queue.push(d + senate.length);
  }

  if (r_queue.length > 0) return "Radiant";
  return "Dire";
};

// Time: O(n)
// Space: O(n)
