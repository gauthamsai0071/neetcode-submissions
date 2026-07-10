class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        '''
        Monotonic decreasing Stack
        we append idx,temp onto a new stack to track the 
        ans=0,0,0,0,0,0,0
        arr = 30,38,30,29,28,40,28
        stack=[[0,30]]; i=0
        i=1; 38
        [[0,30],[1,38]]  we notice the arr[i]>stack[-1][1]
        so we pop the stack and add ans[i]= i-stack[-1][0]
        stack=[]
        i=2; 30
        stack=[[30,2]]
        i=3; 29
        stack=[[30,2],[29,3]]
        i=4; 28
        stack=[[30,2],[29,3],[28,4]]
        i=5; 40
        we notice stack[-1][0]<40
        so we enter the while loop and begin popping
        '''
        n=len(temps);stack=[]; ans=[0]*n
        for i in range(n):
            
            while stack and stack[-1][1]<temps[i]:
                stackIdx, stackTemp = stack.pop()
                ans[stackIdx]=(i-stackIdx)
                
            stack.append([i,temps[i]])

        return ans
