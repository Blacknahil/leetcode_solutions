class CustomStack:

    def __init__(self, maxSize: int):
        self.max=maxSize
        self.stack=[0]*maxSize
        self.incre_arr=[0]*maxSize
        self.lastIndex=-1

    def push(self, x: int) -> None:
        if self.lastIndex<self.max-1:
            self.lastIndex+=1
            self.stack[self.lastIndex]=x
            
        
    def pop(self) -> int:
        if self.lastIndex<0:
            return -1

        cur=self.incre_arr[self.lastIndex]+self.stack[self.lastIndex]
        if self.lastIndex>0:
            self.incre_arr[self.lastIndex-1]+=self.incre_arr[self.lastIndex]
        self.incre_arr[self.lastIndex]=0
        self.lastIndex-=1
        return cur


    def increment(self, k: int, val: int) -> None:
        if self.lastIndex>=0:
            index=min(k-1,self.lastIndex)
            self.incre_arr[index]+=val

        
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)