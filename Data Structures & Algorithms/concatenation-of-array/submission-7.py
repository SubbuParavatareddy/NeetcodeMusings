class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (n * 2)
        for idx, num in enumerate(nums):
            ans[idx] = ans[idx + n] = nums[idx]
        return ans