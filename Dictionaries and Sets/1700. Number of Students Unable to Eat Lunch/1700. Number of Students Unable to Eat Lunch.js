/**
 * @param {number[]} students
 * @param {number[]} sandwiches
 * @return {number}
 */
var countStudents = function (students, sandwiches) {
  let ans = students.length;

  const counter = { 0: 0, 1: 0 };
  for (const s of students) {
    counter[s]++;
  }

  for (const s of sandwiches) {
    if (counter[s] <= 0) return ans;
    counter[s]--;
    ans--;
  }

  return ans;
};

// Time: O(n)
// Space: O(1)
