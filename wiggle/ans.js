/**
 * @param {number[]} nums
 * @return {number}
 */
var wiggleMaxLength = function(nums) {
    if(nums.length === 0) return 0; // empty list case
    var length = 1;
    var previous = nums[0];
    var direction; // true means up or positive difference
    for(var cur = 1;cur < nums.length; cur++) {
        if(previous !== nums[cur]) {
            if(direction !== (previous < nums[cur])) {
                direction = previous < nums[cur];
                previous = nums[cur];
                length++;
            }
            else {
                previous = nums[cur];
            }
        }
    }
    return length;
};
