class MinStack:

    def __init__(self):
        self.stack=[]
        self.minval=float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        self.minval=self.stack[0]
        for i in range(len(self.stack)):
            self.minval=min(self.minval,self.stack[i])
        return self.minval if self.minval!=float("infinity") else None
