from util import check
import math

class Solution:
    def coinChange_new(self, coins, amount):
        coins.sort(reverse=True)
        self.min_length=math.inf
        # (no of coins used so far, amount to make, using coins, coin list)
        self.coinChange_rec(0,amount, coins)
        return  self.min_length if not self.min_length==math.inf else -1

    def coinChange_rec(self, count, amount, coins):
        if len(coins)==0:
            return
        poss=amount//coins[0]
        if amount%coins[0]==0:
            self.min_length=min(count+poss,self.min_length)

        for p in range(poss,-1,-1):
            if count+p<self.min_length:
                self.coinChange_rec(count+p,amount-p*coins[0],coins[1:])
            else:
                break
        return self.min_length



    def coinChange(self, coins, amount: int) -> int:

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
check([[1,2,3], 5], [2], sol.coinChange_new)
check([[1,2,3], 11], [4], sol.coinChange_new)
check([[2], 3], [-1], sol.coinChange_new)
check([[1], 0], [0], sol.coinChange_new)
check([[1,2,5], 100], [20], sol.coinChange_new)
check([[2,5,10,1], 27], [4], sol.coinChange_new)
check([[186,419,83,408], 6249], [20], sol.coinChange_new)
check([[3,7,405,436], 8839], [25], sol.coinChange_new)
check([[470,35,120,81,121], 9825], [30], sol.coinChange_new)
check([[346,29,395,188,155,109], 9401], [26], sol.coinChange_new)
check([[470,18,66,301,403,112,360], 8235], [20], sol.coinChange_new)