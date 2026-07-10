class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            print(stack)
            if tokens[i]=='+':
                a=int(stack.pop())
                b=int(stack.pop())
                c=b+a
                stack.append(c)
            elif tokens[i]=='-':
                a=int(stack.pop())
                b=int(stack.pop())
                c=b-a
                stack.append(c)
            elif tokens[i]=='*':
                a=int(stack.pop())
                b=int(stack.pop())
                c=b*a
                stack.append(c)
            elif tokens[i]=='/':
                a=int(stack.pop())
                b=int(stack.pop())
                c=int(b/a)
                stack.append(c)
            else:
                stack.append(tokens[i])
            print(stack)
        return int(stack[0])