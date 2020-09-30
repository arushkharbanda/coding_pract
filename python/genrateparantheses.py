

from datetime import datetime
from math import floor

verbose=True
def debug(msg):
    if verbose:
        print(msg)



class Solution:
    def generateParenthesis(self, n: int):
        if n<1:
            return []
        else:
            stack=[('(',(1,0))]
            result=set()
            while(len(stack)>0):
                e, count=stack.pop()
                open, closed=count
                if (open<n):
                    e1=e+'('
                    open_new=open+1
                    stack.append((e1,(open_new, closed)))
                if open>closed:
                    e2=e+')'
                    closed_new=closed+1
                    stack.append((e2,(open, closed_new)))
                if open==n and closed==n:
                    result.add(e)
            return result



sol=Solution()

def check(a,b):
    dt = datetime.now()
    start=dt.microsecond
    output=sol.generateParenthesis(a)
    dt = datetime.now()
    end=dt.microsecond
    print("output {} for {} expected {} took time {}".format(len(output),a,len(b),(end-start)))
    #assert(output==b)


check(0,[])
check(-1,[])
check(3,["((()))","(()())", "(())()", "()(())", "()()()"])
check(4,[])
check(9,[])
check(20,[])
#check(39, [])
#check(58,[])
#check(1994,[])
#check(2421,[])

