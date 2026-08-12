/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxSubarrayLength = function (nums, k) {
    counter = {}
    left = 0
    len = 0
    for (let i = 0; i < nums.length; i++) {
        let n = nums[i];
        if (n in counter) counter[n] += 1;
        else counter[n] = 1;
        
        if (counter[n] <= k) {
            len = Math.max(len, i + 1 - left)
            continue
        }

        while (counter[n] > k) {
            counter[nums[left]] -= 1
            left += 1
        }
    }

    return len
};