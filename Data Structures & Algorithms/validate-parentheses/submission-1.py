class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for i in s:
            stack.append(i)
            if stack[-1]==')':
                if len(stack)>1 and stack[-2]=='(':
                    stack.pop()
                    stack.pop()
            elif stack[-1]=='}':
                if len(stack)>1 and stack[-2]=='{':
                    stack.pop()
                    stack.pop()
            elif stack[-1]==']':
                if len(stack)>1 and stack[-2]=='[' :
                    stack.pop()
                    stack.pop()
                
        return len(stack)==0
