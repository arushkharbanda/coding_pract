from datetime import datetime
from math import floor


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        nminus1=None
        nminus2=None
        for n in reversed(nums):
            if n==nminus1 and n==nminus2:

        for

sol=Solution()

def check(a,b, c):
    dt = datetime.now()
    start=dt
    output=sol.threeSumClosest(a, b)
    dt = datetime.now()
    end=dt
    print("output {} for {}-{} expected {} took time {}".format(len(output),a,b,c,(end-start)))
    print(end-start)
    assert(output==c)



check([-1,2,1,-4],-1,[2,1,-4])
