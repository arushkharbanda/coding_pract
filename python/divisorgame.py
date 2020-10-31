from util import check
class Solution:
    def __init__(self):
        self.pre_calc=[False for i in range(1001)]
        self.factors_list={}
    def factors(self, n):
        if n not in self.factors_list.keys():
            f=[]
            for i in range(1, (n//2)+1):
                if n%i==0:
                    f.append(i)
            self.factors_list[n]=f
            #print("calculated factors of {}".format(n))
        else:
            f=self.factors_list[n]
        return f
    def divisorGame(self, N: int) -> bool:
        for i in range(2,N+1):
            f=self.factors(i)
            options=[i-factor for factor in f ]
            res=False
            for option in options:
                res=(not self.pre_calc[option]) or res
            self.pre_calc[i]=res
        return self.pre_calc[N]

sol=Solution()
for i in range(1,1000):
    if not sol.divisorGame(i)==(i%2==0):
        check([i],[i%2==0], sol.divisorGame)

check([3],[False], sol.divisorGame)
check([20],[True], sol.divisorGame)
check([1000],[True], sol.divisorGame)