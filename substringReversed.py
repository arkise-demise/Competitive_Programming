class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        i=0
        while (i<len(s)):
            if s[i]!=')':
                stack.append(s[i])
            else:
                stackpoppedEle=[]
                while (stack[-1]!='('):
                    stackpoppedEle.append(stack.pop())
                stack.pop()
                stack.extend(stackpoppedEle)
            i+=1
        return "" .join(stack)
