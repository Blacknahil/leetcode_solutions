class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        m=len(grid[0])
        ans=[[0]*(m-2) for _ in range(n-2)]

        def find_largest(r_start,c_start):
            largest=0
            for r in range(r_start,r_start+3):
                for c in range(c_start,c_start+3):
                    largest=max(largest,grid[r][c])
            ans[r_start][c_start]=largest
            return
        
        for r in range(n-2):
            for c in range(m-2):
                find_largest(r,c)
        return ans