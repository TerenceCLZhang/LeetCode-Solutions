/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
    let low = 1
    let high = Math.max(...piles)

    while (low <= high) {
        const k = Math.floor((low + high) / 2)
        const curr_time = piles.reduce((a, c) => a + Math.ceil(c / k), 0)
        if (curr_time <= h) high = k - 1
        else low = k + 1
    }

    return low
};

// Time: O(n log max(piles))
// Space: O(1)
