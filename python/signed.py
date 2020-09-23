from datetime import datetime
from math import pow, floor

verbose=True
def debug(msg):
    if verbose:
        print(msg)

class Solution:
    def reverse(self, x: int) -> int:
        inpStr=str(x)
        outputStr=""



        if x<0:
            outputStr="-"
            x=x*-1
        while(x!=0):
            rem=x%10
            x=floor(x/10)
            outputStr=outputStr+str(rem)

        if outputStr=="" or outputStr=="-":
            outputStr="0"

        result=int(outputStr)
        if result <= -2147483647 or result >= 2147483646:
            return 0

        return int(outputStr)



sol=Solution()



def check(a,b):
    dt = datetime.now()
    start=dt.microsecond
    output=sol.reverse(a)
    dt = datetime.now()
    end=dt.microsecond
    print("output {} for {} expected {} took time {}".format(output,a,b,(end-start)))
    assert(output==b)


#check(123,321)
#check(-123,-321)
#check(120,21)
check(int(pow(2,31)*-1),0)
#check(1534236469,0)
check(2147483647,0)
#check(0,0)
#check(-0,0)
#check(10,1)
