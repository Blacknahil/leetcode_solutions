class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        candies=[1 for _ in range(n)]
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                candies[i]=candies[i-1]+1
        for j in range(n-2,-1,-1):
            if ratings[j]>ratings[j+1]:
                candies[j]=max(candies[j],candies[j+1]+1)

        print(candies)
        return sum(candies)


        