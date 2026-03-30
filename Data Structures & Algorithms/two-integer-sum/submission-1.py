class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, val1 in enumerate(nums):
            for idx2 in range(idx1 + 1, len(nums)):
                val2 = nums[idx2]
                if val1 + val2 == target:
                    return [idx1, idx2]
        return [0, 0]