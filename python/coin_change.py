from util import check
import math
import sys

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        # create empty array with max_int
        arr_sub=[math.inf for i in range(len(coins))]
        arr=[arr_sub.copy() for i in range(amount+1)]
        #arr is [amount+1][len(coins)] max_int
        for p in range(0,len(coins)):
            arr[0][p]=0
        for i, ele in enumerate(coins):
            for sum in range(1,amount+1):
                if sum<ele:
                    with_ele=math.inf
                else:
                    with_ele=arr[sum-ele][i]+1

                if i!=0:
                    without=arr[sum][i-1]
                else:
                    without=math.inf
                arr[sum][i]=min(with_ele, without)

        result=min(arr[amount])
        return result if result!=math.inf else -1


sol=Solution()
check([[1,2,5], 11], [3], sol.coinChange)
check([[1,2,3], 5], [2], sol.coinChange)
check([[1,2,3], 11], [4], sol.coinChange)
check([[2], 3], [-1], sol.coinChange)
check([[1], 0], [0], sol.coinChange)
