/**
 * @param {number} n
 * @return {boolean}
 */
var isUgly = function(n) {
    if (n <= 0) return false
    for (let i of [2, 3, 5]) {
        while (n % i == 0) {
            n = Math.floor(n / i)
        }
    }
    return n === 1
};

// Time: O(log n)
// Space: O(1)
