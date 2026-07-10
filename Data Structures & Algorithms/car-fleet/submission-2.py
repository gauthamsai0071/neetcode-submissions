class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        '''
        1+3->4+3->7+3
        4+2->6+2->8+2

        need to understand how many steps i takes to reach target

        4+2->6+2->8+2
        1+2->3+2->5+2->7+2->9+2
        0+1->1+1.... 10 steps
        7+1->8+1->9+1

        target=12.                 steps=[]
        position=[10,8,0,5,3]
        speed=[2,4,1,1,3]
        10+2             steps=[[10,1]]
        8+4             steps=[[10,1],[8,1]]
        0+1->1+1...             steps=[[8,1],[0,12]]
        5+1->6+1->...             steps=[[8,1],[0,12],[5,7]]
        3+3->6+3->9+3             steps=[[8,1],[0,12],[5,7],[3,3]]

        steps = (target-initial_position)//speed

        we need to understand if pos[i]>pos[j] and if steps[j]<steps[i]; 
        final steps[j]=steps[i] as pos[j] is behind pos[i], and cars cannot overtake
        
        '''
        steps=[]; n=len(pos)
        cars=[[pos[i],speed[i]] for i in range(n)]
        cars.sort(key=lambda x:x[0], reverse=True)
        for pos,sp in cars:
            s=(target-pos)/sp
            # we are tracking the arrival time for higest positioned car 
            if not steps or s>steps[-1][1]:
                steps.append([pos,s])
        return len(steps)