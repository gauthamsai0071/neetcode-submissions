class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums);ans=[];nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target=-nums[i]
            left=i+1;right=n-1
            while(left<right):
                if nums[left]+nums[right]==target:
                    ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif nums[left]+nums[right]>target:
                    right-=1
                else:
                    left+=1
        return ans