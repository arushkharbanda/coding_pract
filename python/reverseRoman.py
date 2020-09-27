

from datetime import datetime
from math import floor

verbose=True
def debug(msg):
    if verbose:
        print(msg)



class Solution:
    def romanToInt(self, s: str) -> int:
        list={'M':1000, 'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        result=0
        previous=0
        for c in s[::-1]:
            if c in list.keys():
                a=list[c]
                if a>=previous:
                    result=result+a
                else:
                    result=result-a
                previous=a
        return result


sol=Solution()

def check(b,a):
    dt = datetime.now()
    start=dt.microsecond
    output=sol.romanToInt(a)
    dt = datetime.now()
    end=dt.microsecond
    print("output {} for {} expected {} took time {}".format(output,a,b,(end-start)))
    #assert(output==b)


check(3,'III')
check(4,'IV')
check(9,'IX')
check(58,'LVIII')
check(1994,'MCMXCIV')
check(39, 'XXXIX')
check(2421,'MMCDXXI')

