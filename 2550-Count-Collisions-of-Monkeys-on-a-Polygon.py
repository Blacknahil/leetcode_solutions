class Solution:
    def monkeyMove(self, n: int) -> int:
        visited={}
        def power(p):
            if p==0:
                return 1
            if p==1:
                return 2
            if p in visited:
                return visited[p]
            if p%2==0:
                res=power(p//2)*power(p//2)
            else:
                res=2*power(p//2)*power(p//2)
            res%=(10**9 +7)
            visited[p]=res
            return res

        ans=power(n)
        ans=(ans-2)%(10**9 +7)
        return ans
        