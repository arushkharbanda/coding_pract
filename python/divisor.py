from util import check

class Solution:
    def factors(self, n):
        f=[]
        for i in range(1, (n//2)+1):
            if n%i==0:
                f.append(i)
        return f
    def divisorGame(self, N: int) -> bool:
        pre_calc=[False for i in range(N+1)]
        for i in range(2,N+1):
            f=self.factors(i)
            options=[i-factor for factor in f ]
            res=False
            for option in options:
                res=(not pre_calc[option]) or res
            pre_calc[i]=res
        return pre_calc[N]


sol=Solution()
check([2],[True], sol.divisorGame)
check([3],[False], sol.divisorGame)
check([4],[True], sol.divisorGame)
check([5],[False], sol.divisorGame)
check([6],[True], sol.divisorGame)
check([7],[False], sol.divisorGame)
check([1000],[True], sol.divisorGame)