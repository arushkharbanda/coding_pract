from util import check
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividend_b="{0:b}".format(dividend)
        divisor=="{0:b}".format(divisor)

sol=Solution()
check([10,3],[3], sol.divide)
check([7,-3],[-2], sol.divide)
check([0,1],[0], sol.divide)
check([1,1],[1], sol.divide)