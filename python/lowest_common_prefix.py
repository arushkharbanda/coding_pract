

from datetime import datetime
from math import floor

verbose=True
def debug(msg):
    if verbose:
        print(msg)



class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs)>0:
            lcp=strs[0]
        else:
            lcp=''
        for s in strs[1:]:
            newlcp=""
            for i,c in enumerate(s):
                if(len(lcp)>i):
                    if c == lcp[i]:
                        newlcp=newlcp+c
                    else:
                        break
            lcp=newlcp
            if lcp=='':
                break
        return lcp


sol=Solution()

def check(a,b):
    dt = datetime.now()
    start=dt.microsecond
    output=sol.longestCommonPrefix(a)
    dt = datetime.now()
    end=dt.microsecond
    print("output {} for {} expected {} took time {}".format(output,a,b,(end-start)))
    assert(output==b)


check(["flower","flow","flight"],'fl')
check(["dog","racecar","car"],'')
check(["arush","arus","aru","ar","a"],'a')
check([],'')

