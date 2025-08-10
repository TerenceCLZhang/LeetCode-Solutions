class Solution {

  public int hIndex(int[] citations) {
    int n = citations.length;
    int[] numCitations = new int[n + 1];

    for (int c : citations) {
      numCitations[Math.min(c, n)]++;
    }

    int papers = 0;
    for (int h = n; h > -1; h--) {
      papers += numCitations[h];
      if (papers >= h) {
        return h;
      }
    }

    return 0;
  }
}
