class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original)!=m*n:
            return []
        res=[]
        start=0
        for _ in range(m):
            res.append(original[start:start+n])
            start+=n
        return res
        