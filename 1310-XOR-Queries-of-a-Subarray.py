class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix=[0]
        for num in arr:
            prefix.append(prefix[-1]^num)
        ans=[]
        for left,right in queries:
            ans.append(prefix[left]^prefix[right+1])
            
        return ans