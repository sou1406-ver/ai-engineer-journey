class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans={}
        for i in strs: 
            ans["".join(sorted(i))]=[]
        for i in strs:
            ans["".join(sorted(i))].append(i)
        return list(ans.values())