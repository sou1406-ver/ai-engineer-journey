class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        tmp={}
        for i in range(len(nums)): 
            tmp[target-nums[i]]=i
        for i in range(len(nums)):
            if nums[i] in tmp and tmp[nums[i]]!=i: 
                return [i, tmp[nums[i]]]