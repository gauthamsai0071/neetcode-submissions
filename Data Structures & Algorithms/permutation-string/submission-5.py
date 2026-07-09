class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        we calculate the freq of smallest among s1 and s2 assume s1

        then we move onto the s2 with:
        start with left,right=0,0
        out max window to check is min(len(s1,s2)); 
        if the freq of s2 in that window matches with s1 return true
        '''

        l1=len(list(s1));l2=len(list(s2))
        checkfreq={};window=0
        for i in range(l1):
            checkfreq[s1[i]]=checkfreq.get(s1[i],0)+1
            window+=1

        s=s2
        for i in range(len(s)-window+1):
            freq={}; j=i; ans=1
            while(j<i+window):
                freq[s[j]]=freq.get(s[j],0)+1
                if s[j] in checkfreq:
                    if checkfreq[s[j]]<freq[s[j]]:
                        ans=0
                        break
                else:
                    ans=0
                    break
                j+=1
                
            if ans==1:
                return True
        return False
            
