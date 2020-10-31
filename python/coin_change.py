from util import check
import math
import sys
from collections import deque

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        s=deque()
        coins.sort(reverse=True)
        min_coin=coins[0]
        # steps, sum and list
        s.append((0, 0,[]))
        if amount==0:
            return 0
        while s:
            steps,old_sum, coin_list=s.popleft()
            #print("got sum {}, steps {} and list {} from stack".format(old_sum,steps,coin_list))
            steps=steps+1
            for coin in coins:
                new_sum=old_sum+coin
                new_coin_list=coin_list.copy()
                new_coin_list.append(coin)
                if new_sum<=amount-min_coin:
                    s.append((steps,new_sum,  new_coin_list))
                if new_sum==amount:
                    #print("list {}".format(new_coin_list))
                    return steps

        return -1

    def coinChange_new(self, coins, amount: int) -> int:

            self.ans = float('inf')

            # Start searching from the biggest coin
            coins.sort(reverse=True)
            self.dfs(coins, amount, 0)
            return -1 if self.ans == float('inf') else self.ans


    def dfs(self, coins, amount, prev_count):
        """
        Recursive DFS function to seach valid coins combination.
        First is to use greedy method find out a potential-best solution.
        Then start to search the second biggest coin with pruning when the coins number >= the potential-best solution.

        Args:
            coins: coins list from which we pick coins into combination
            amount: target amount
            prev_count: number of coins picked before this round

        """
        # Set up stop condtion
        if len(coins) == 0:
            return

        if amount % coins[0] == 0:
            # Update potential answer
            self.ans = min(self.ans, prev_count + amount // coins[0])
        else:
            for k in range(amount // coins[0], -1, -1):
                # Set up pruning condtion
                if prev_count + k >= self.ans:
                    break
                self.dfs(coins[1:], amount - k * coins[0], prev_count + k)




sol=Solution()
check([[1,2,5], 11], [3], sol.coinChange_new)
#check([[1,2,3], 5], [2], sol.coinChange)
#check([[1,2,3], 11], [4], sol.coinChange)
#check([[2], 3], [-1], sol.coinChange)
#check([[1], 0], [0], sol.coinChange)
#check([[1,2,5], 100], [20], sol.coinChange_new)
#check([[2,5,10,1], 27], [4], sol.coinChange_new)
#check([[186,419,83,408], 6249], [20], sol.coinChange_new)

