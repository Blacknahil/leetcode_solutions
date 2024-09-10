class Solution:
    def calculate(self, s: str) -> int:
        n=len(s)
        operations=set([\*\,\/\,\+\,\-\])
        def helper(arr,sign):
            stack=[]
            i=0
            while i<len(arr):
                char=arr[i]
                if char.isnumeric():
                    if stack and stack[-1].isnumeric():
                        stack[-1]+=char
                    else:
                        stack.append(char)
                    i+=1
                elif char==\ \:
                    i+=1
                    continue
                elif char!=sign:
                    i+=1
                    stack.append(char)
                else:
                    temp=\\
                    right=i+1
                    while right<len(arr):
                        if arr[right].isnumeric():
                            temp+=arr[right]
                            right+=1
                        elif arr[right]==\ \:
                            right+=1
                        else:
                            break
                    i=right
                    left=stack.pop()
                    if stack and stack[-1]==\-\:
                        left=stack.pop()+left

                    if sign==\*\:
                        res=int(left)*int(temp)
                    elif sign==\/\:
                        if int(left)<0:
                            res=-1*(abs(int(left))//int(temp))
                        else:
                            res=int(left)//int(temp)
                    elif sign==\+\:
                        res=int(left)+int(temp)
                    else:
                        res=int(left)-int(temp)
                    
                    if stack and stack[-1].isnumeric():
                        if res>=0:
                            stack.append(\+\)
                            stack.append(str(res))

                        else:
                            stack.append(\-\)
                            stack.append(str(abs(res)))
                    if stack and stack[-1]==\+\ and res<0:
                        stack.pop()
                        stack.append(\-\)
                        stack.append(str(abs(res)))
                    else:
                        stack.append(str(res))
            return stack
        temp=list(s)
        while len(temp)!=1:
            temp=helper(temp,\/\)
            temp=helper(temp,\*\)

            temp=helper(temp,\+\)
            temp=helper(temp,\-\)
            
        return int(temp[0])
        

        