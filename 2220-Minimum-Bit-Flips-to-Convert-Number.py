class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count=0
        while start and goal:
            #checking if their last bit is the same or not
            if (1&start) ^(1&goal)==1:
                count+=1
            #shifting the last bit to the right 
            start>>=1
            goal>>=1
        #checking if there is any remaining bits which is not found on both numbers
        
        res=start if start else goal
        while res:
            #checking if the last bit 0.
            #if it is 0 add one to count
            count+=(0^(res&1))
            res>>=1
        
        return count

        