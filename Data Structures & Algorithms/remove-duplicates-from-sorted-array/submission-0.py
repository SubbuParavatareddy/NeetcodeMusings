class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = 0
        new_nums = nums
        for i, num in enumerate(nums):
            if i < len(nums) - 1 and nums[i] == nums[i+1]:
                continue
            else:
                new_nums[res] = nums[i]
                res += 1

        return res 
