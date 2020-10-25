from util import check
from collections import deque
class Solution:

    def prisonAfterNDays(self, cells, N: int):
        base=cells.copy()
        statelist=[]
        #statelist.append(cells)
        zeroarray=[0 for x in range(8)]
        for i in range(N):
            forward=zeroarray.copy()
            for j in range(1,len(cells)-1):
                forward[j] = 1 -( base[j-1] ^ base[j+1])
            if len(statelist)>1:
                if forward == statelist[0]:
                    # after i+1 steps we reached the same where we started
                    remainingsteps=N-i
                    rem=remainingsteps%(len(statelist))
                    return statelist[rem-1]
            statelist.append(forward)
            base=forward
        return forward




sol=Solution()
check([[0,1,0,1,1,0,0,1], 7],[[0, 0, 1, 1, 0, 0, 0, 0]] ,sol.prisonAfterNDays) #51
check([[1,0,0,1,0,0,1,0], 10],[[0, 1, 0, 0, 1, 1, 1, 0]], sol.prisonAfterNDays) #44
check([[1,0,0,1,0,0,1,0], 20],[[0,0,1,1,1,1,1,0]], sol.prisonAfterNDays) #44
check([[1,0,0,1,0,0,1,0], 30],[[0,1,0,1,0,0,1,0]], sol.prisonAfterNDays) #44
check([[1,0,0,1,0,0,1,0], 100],[[0, 1, 0, 1, 0, 0, 1, 0]], sol.prisonAfterNDays) #390
check([[1,0,0,1,0,0,1,0], 1000],[[0, 0, 1, 1, 1, 1, 1, 0]], sol.prisonAfterNDays) #3872
check([[1,0,0,1,0,0,1,0], 10000],[[0, 0, 1, 0, 0, 0, 1, 0]], sol.prisonAfterNDays) #38807
check([[1,0,0,1,0,0,1,0], 100000],[[0,0,1,1,1,1,1,0]], sol.prisonAfterNDays) #371428
check([[1,0,0,1,0,0,1,0], 1000000],[[0,0,1,1,1,1,1,0]], sol.prisonAfterNDays)
check([[1,0,0,1,0,0,1,0], 10000000],[[0,0,1,1,1,1,1,0]], sol.prisonAfterNDays) #299330
check([[1,0,0,1,0,0,1,0], 100000000],[[0,0,1,1,1,1,1,0]], sol.prisonAfterNDays) #357282
check([[1,0,0,1,0,0,1,0], 1000000000],[[0,0,1,1,1,1,1,0]], sol.prisonAfterNDays)