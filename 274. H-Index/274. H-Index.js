/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function (citations) {
  const n = citations.length;
  const numCitations = new Array(n + 1).fill(0);

  for (const c of citations) {
    numCitations[Math.min(c, n)]++;
  }

  let papers = 0;
  for (let h = n; h > -1; h--) {
    papers += numCitations[h];
    if (papers >= h) {
      return h;
    }
  }
};
