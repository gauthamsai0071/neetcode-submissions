class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        0,1,1,2,3,4,5,6
        3,5,6,7,8,10
        '''

        numSet=set(nums);length=1;longest=0;curr=0
        for num in numSet:
            if num -1 not in numSet:
                curr=num
                length =1
            while curr+1 in numSet:
                length+=1
                curr+=1
            longest=max(longest,length)
        return longest
            