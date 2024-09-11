class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD=10**9 +7
        total_ways=pow(2,n,MOD)
        noCollison=2
        return (total_ways-noCollison)%MOD
        