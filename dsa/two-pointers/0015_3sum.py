class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        tmp=sorted(nums)
        ans=[]
        for i in range(len(tmp)):
            if i>0 and tmp[i]==tmp[i-1]: continue
            r=len(tmp)-1
            l=i+1
            while l<r : 
                if tmp[l]+ tmp[r]> -tmp[i]:  
                    r-=1
                elif tmp[l]+ tmp[r]< -tmp[i]:   
                    l+=1
                else: 
                    ans.append([tmp[i], tmp[l], tmp[r]])
                    while l<r and tmp[l]==tmp[l+1] : l+=1
                    while l<r and tmp[r]==tmp[r-1] : r-=1
                    l+=1
                    r-=1
        return ans