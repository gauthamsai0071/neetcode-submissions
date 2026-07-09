class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        0,0
        0,1
        0,2
        1,3
        '''
        freq={};n=len(nums);ans=[]
        l=0;r=0
        while(r<n):
            freq[nums[r]]=freq.get(nums[r],0)+1
            if r-l+1==k:
                t=float("-infinity")
                for f in freq:
                    if freq[f]>0:
                        t=max(t,f)
                ans.append(t)
                # print(nums[l:r+1],freq)
                freq[nums[l]]-=1
                
                r+=1
                l+=1
            else:
                r+=1
        return ans
                
