class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        e=0
        ones=0
        for i in range(1,n+1):
            if i==2**e:
                ones=1
                e+=1
            else:
                ones+=1
            ans.append(ones)

        return ans