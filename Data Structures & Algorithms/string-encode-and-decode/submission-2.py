class Solution:

    def encode(self, strs: List[str]) -> str:
        n=len(strs); encode_str=''
        for i in range(n):
            chars=list(strs[i])
            encode_str+=str(len(chars))+'#'+strs[i]
        return encode_str
            

    def decode(self, st: str) -> List[str]:
        chars=list(st); n=len(chars)
        ans=[]
        i=0
        while(i<n):
            j=i
            while st[j]!='#':
                j+=1
            s_len=int(st[i:j])
            ans.append(st[j+1:j+s_len+1])
            i=j+s_len+1
        
        return ans