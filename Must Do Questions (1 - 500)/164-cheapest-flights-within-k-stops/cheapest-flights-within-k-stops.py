class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = collections.defaultdict(lambda: math.inf)
        cost[src] = 0
        for _ in range(k + 1):
            temp_cost = cost.copy()
            for frm, to, price in flights:
                if temp_cost[to] > cost[frm] + price:
                    temp_cost[to] = cost[frm] + price
            cost = temp_cost

        return cost[dst] if cost[dst] != math.inf else -1