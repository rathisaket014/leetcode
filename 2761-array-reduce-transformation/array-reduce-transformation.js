/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let ans = init

    for (let num = 0; num < nums.length; num++) {
        ans = fn(ans, nums[num])
    }

    return ans
};