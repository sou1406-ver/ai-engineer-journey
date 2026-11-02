class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        snums=sorted(nums)
        tmp=1
        if len(nums)==0: return 0
        ans=1
        for i in range(len(snums)-1):
            if snums[i+1]==snums[i]+1: 
                tmp+=1
                ans=max(ans, tmp)
            elif snums[i+1]==snums[i]:
                continue 
            else: 
                tmp=1
        return ans