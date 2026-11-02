class Solution(object):
    def containsDuplicate(self, nums):
        tmp=set(nums)
        if len(nums) == len(tmp):  return False
        else: return True