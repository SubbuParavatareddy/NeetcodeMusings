class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create set, assign nums
        # if len of set is less than nums. array has duplicate

        nums_set = set(nums)
        if len(nums_set) < len(nums):
            return True
        return False
