class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # visited=?
        # heapq ---> cost,stops,where am i?, 
        graph=defaultdict(list)
        for u,v,cost in flights:
            graph[u].append((v,cost))
        
        heap=[(0,0,src)]
        visited=set()
        while heap:
            cost,stops,node=heapq.heappop(heap)
            if node==dst:
                return cost
            
            if stops>k:
                continue
            for nbr,nbr_cost in graph[node]:
                if (nbr,cost+nbr_cost) not in visited:
                    visited.add((nbr,cost+nbr_cost))
                    heapq.heappush(heap,(cost+nbr_cost,stops+1,nbr))
        
        return -1



        