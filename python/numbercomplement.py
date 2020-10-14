from util import check

class Solution:
    def findComplement(self, num: int) -> int:
        x=1
        while x-1<num:
            x=x*2
        xor_with=x-1
        return xor_with^num

sol=Solution()
check([5],2,sol.findComplement)
check([1],0,sol.findComplement)
check([20],0,sol.findComplement)
check([1],0,sol.findComplement)
check([1],0,sol.findComplement)
check([1],0,sol.findComplement)
check([1],0,sol.findComplement)