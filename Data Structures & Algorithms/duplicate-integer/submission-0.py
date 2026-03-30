class Solution:
    def hasDuplicate(self, nums):
        a=set(nums)
        if (len(a)!=len(nums)):
            return True
        else:
            return False
