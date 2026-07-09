class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0;n=len(list(s))
        ans=0; 
        while(i<n):
            seen={};j=i+1
            seen[s[i]]=1
            while(j<n and s[j] not in seen):
                seen[s[j]]=1
                j+=1
            ans=max(ans,j-i)
            i+=1
        return ans