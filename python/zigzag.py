from datetime import datetime
from math import floor


verbose=True
def debug(msg):
    if verbose:
        print(msg)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l=len(s)

        ansArrs=["" for i in range(0,numRows)]

        # No of elements per set
        k=(2*numRows-2)
        if k<=0:
            k=1

        ans=""
        for j in range(0, l):
            rem=j%k
            if rem<numRows:
                stack=rem
            else:
                stack=numRows-(rem%numRows)-2

            ansArrs[stack]=ansArrs[stack]+s[j]
            #debug("Adding {} Current Arrays {}".format(s[j],ansArrs))
        for k in range(0, len(ansArrs)):
            ans=ans+"".join(ansArrs[k])
        return ans




sol=Solution()





def check(a,b,c):
    dt = datetime.now()
    start=dt.microsecond
    output=sol.convert(a, b)
    dt = datetime.now()
    end=dt.microsecond
    print("output {} for {}-{} expected {} took time {}".format(output,a,b,c,(end-start)))
    assert(output==c)


check("PAYPALISHIRING",3,"PAHNAPLSIIGYIR")
check("PAYPALISHIRING",4,"PINALSIGYAHRPI")
check("",4,"")
check("A",1,"A")