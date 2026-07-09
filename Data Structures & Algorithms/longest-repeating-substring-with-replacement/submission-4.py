class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        we need to find the sequence where 
        we have atmost k non most frequent chars
        
        '''
        n=len(list(s)); ans=0; 
        s=list(s)
        for left in range(n):
            freq={}
            freq[s[left]]=1
            maxFreq=1
            for right in range(left+1,n):
                freq[s[right]]=freq.get(s[right],0)+1
                maxFreq=max(maxFreq, freq[s[right]])
                window=right-left+1
                if window-maxFreq<=k:
                    ans=max(ans,window)
                else:
                    break
        return ans