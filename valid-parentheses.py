class Solution:
    def isValid(self, s: str) -> bool:
        def match(stack,char):
            if stack[-1]=='(' and  char==')':
                return 1
            if stack[-1]=='[' and char==']':
                return 1
            if stack[-1]=='{' and char=='}':
                return 1
            return 0
        
        stack=[]
        for i in range(0,len(s)):
            if s[i] in ('(','{','['):
                stack.append(s[i])
            elif s[i] in (')','}',']'):
                if(len(stack)!=0):
                    if match(stack,s[i]):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
            
        
        
