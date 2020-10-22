from util import check

pre_calc={0:1,1:1,2:1}
class Solution:
    def fib(self, N: int) -> int:
        if N in pre_calc.keys():
            return pre_calc[N]
        else:
            for i in range(2,N):
                if i+1 in pre_calc.keys():
                    continue
                else:
                    pre_calc[i+1]=pre_calc[i]+pre_calc[i-1]
            return pre_calc[N]



sol=Solution()
check([2],[1],sol.fib)
check([3],[2],sol.fib)
check([4],[3],sol.fib)
check([5],[5],sol.fib)
check([6],[8],sol.fib)
check([7],[13],sol.fib)
check([30],[832040],sol.fib)