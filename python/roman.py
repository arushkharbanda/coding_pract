from datetime import datetime
from math import floor

verbose=True
def debug(msg):
    if verbose:
        print(msg)


class Solution:
    def intToRoman(self, num: int) -> str:
        list=[('M',1000), ('D',500),('C',100),('L',50),('X',10),('V',5),('I',1)]
        list.reverse()
        digit=0
        result=""

        while(num>0):
            additional=""
            rem=num%10
            if rem==4:
                additional=list[(digit*2)][0]+list[(digit*2)+1][0]
            elif rem==9:
                additional=list[(digit*2)][0]+list[(digit*2)+2][0]
            elif rem>5:
                additional=list[(digit*2)+1][0]+"".join([list[digit*2][0] for x in range(0,rem-5)])
            elif rem<5:
                additional="".join([list[digit*2][0] for x in range(0,rem)])
            elif rem==5:
                additional=list[(digit*2)+1][0]
            digit=digit+1
            result=additional+result
            val=floor(num/10)

            num=val
        return result



sol=Solution()

def check(a,b):
    dt = datetime.now()
    start=dt.microsecond
    output=sol.intToRoman(a)
    dt = datetime.now()
    end=dt.microsecond
    print("output {} for {} expected {} took time {}".format(output,a,b,(end-start)))
    assert(output==b)


check(3,'III')
check(4,'IV')
check(9,'IX')
check(58,'LVIII')
check(1994,'MCMXCIV')
check(39, 'XXXIX')
check(2421,'MMCDXXI')
