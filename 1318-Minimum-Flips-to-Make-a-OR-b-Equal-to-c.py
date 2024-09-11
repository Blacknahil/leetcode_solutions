class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count=0
        ab=a|b
        while ab or c:
            print('a',a,"b",b,"ab",ab)
            # if the end of the bits is not the same
            if (1&ab) ^ (1&c)==1:
                if (1&c):
                    count+=1
                else:
                    if (a&1) &(b&1):
                        count+=2
                    else:
                        count+=1
            ab>>=1
            a>>=1
            c>>=1
            b>>=1
        
        return count
        