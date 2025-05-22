/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let seen = new Map()
    for (let i = 0; i < nums.length; i++) {
        if (seen.has(nums[i])) {
            return [seen.get(nums[i]), i]
        }
        seen.set(target - nums[i], i)
    }
};

// Time: O(n)
// Space: O(1)