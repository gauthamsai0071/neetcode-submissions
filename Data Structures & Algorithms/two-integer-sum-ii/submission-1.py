class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            left=i+1
            right=n-1
            while(left<=right):
                mid=(left+right)//2
                if nums[mid]+nums[i]==target:
                    return [i+1,mid+1]
                if nums[mid]+nums[i]>target:
                    right-=1
                if nums[mid]+nums[i]<target:
                    left+=1