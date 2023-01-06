class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs= sorted(costs)
        c=0
        for i in range(len(costs)):
            if costs[i]<= coins:
                coins = coins - costs[i]
                c +=1
            else:
                break
        
        return c