class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        2, 2, 4, 6
        2, 4, 16, 92
        92,48,24,6
        '''
        left=[nums[0]];right=[nums[-1]];n=len(nums)
        for i in range(1,n):
            left.append(left[-1]*nums[i])
        
        for i in range(n-2,-1,-1):
            right.append(right[-1]*nums[i])
        right=right[::-1]
        print(left,right)
        ans=[-1]*n
        ans[0]=right[1];ans[-1]=left[-2]
        for i in range(1,n-1):
            ans[i]=left[i-1]*right[i+1]
        return ans

