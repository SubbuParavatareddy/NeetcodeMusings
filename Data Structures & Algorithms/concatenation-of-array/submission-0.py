class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        ans = [None] * 2 * nums_len
        idx = 0
        for elm in nums:
            ans[idx] = elm
            ans[idx+nums_len] = elm
            idx += 1
        return ans
