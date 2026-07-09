class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        we need to find all t in s;
        so s should atleast be >=len(t)
        we start with window i+len(s) in t and move right
        we start left once we find atleast 1 among in t is found
        '''

        window=len(list(t))
        checkfreq={}
        for i in range(window):
            checkfreq[t[i]]=checkfreq.get(t[i],0)+1
        
        idx=0;n=len(s)
        for i in range(n):
            if s[i] in checkfreq:
                idx=i
                break
        ans=[]
        for i in range(idx,n):
            freq={}
            j=i
            curr=''
            currlen=1
            need=len(checkfreq); have={}; valid=False
            while(j<n):
                curr+=s[j]
                currlen+=1
                if s[j] in checkfreq:
                    freq[s[j]]=freq.get(s[j],0)+1
                    if freq[s[j]]>=checkfreq[s[j]]:
                        have[s[j]]=1
                if len(have)==need:
                    valid=True
                if valid:
                    ans.append([curr,currlen])
                j+=1
        # print(ans)
        ans.sort(key=lambda x:x[1])
        return ans[0][0] if len(ans)>0 else ''