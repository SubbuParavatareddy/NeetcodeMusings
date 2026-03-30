class Solution {
    fun removeDuplicates(nums: IntArray): Int {
        var res = 0

            for (i in nums.indices) {
                if (i < nums.size - 1 && nums[i] == nums[i + 1]) {
                    continue
                } else {
                    nums[res] = nums[i]
                    res++
                }
            }

            return res
    }
}
