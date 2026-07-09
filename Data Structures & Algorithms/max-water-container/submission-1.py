class Solution:
    def maxArea(self, nums: List[int]) -> int:
        '''
        1,7,2,5,4,7,3,6
        1,7,7,7,7,7,7,7
        7,7,7,7,7,7,6,6
        '''

        # left=[nums[0]];right=[nums[-1]];ans=[]
        n=len(nums)
        # for i in range(n):
        #     left.append(max(left[-1],nums[i]))
        
        # for i in range(n-1,-1,-1):
        #     right.append(max(right[-1],nums[i]))
        # right=right[::-1]
        # print(right);print(left)
        # i=0;j=n-1
        # while(i<j):
        #     if left[i+1]>left[i]:
        #         ans.append(min(left[i],right[j])*(j-i))
        #         i+=1
        #     elif right[j-1]>right[j]:
        #         ans.append(min(left[i],right[j])*(j-i))
        #         j-=1
        #     else:
        #         ans.append(min(left[i],right[j])*(j-i))
        #         i+=1
        #         j-=1
        #     print(i,j)
            
        # return max(ans)

        i=0;j=n-1; ans=0
        while(i<j):
            print(i,j)
            if nums[i]<nums[j]:
                ans=max(ans,min(nums[i],nums[j])*(j-i))
                i+=1
            elif nums[i]>nums[j]:
                ans=max(ans,min(nums[i],nums[j])*(j-i))
                j-=1
            else:
                ans=max(ans,min(nums[i],nums[j])*(j-i))
                i+=1
                j-=1
        ans=max(ans,min(nums[i],nums[j])*(j-i))
        return ans
            
                