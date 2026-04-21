class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            cur_sum = max(num, cur_sum + num)
            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum