from datetime import datetime

verbose=True
def debug(msg):
    if verbose:
        print(msg)


class Solution:
    def maxArea(self, height):
        maxarea = 0
        l = 0
        r = len(height) - 1
        while (l < r):
            maxarea = max(maxarea, min(height[l], height[r]) * (r - l))
            if (height[l] < height[r]):
                l=l+1
            else:
                r=r-1
        return maxarea

sol=Solution()

def check(a,b):
    dt = datetime.now()
    start=dt.microsecond
    output=sol.maxArea(a)
    dt = datetime.now()
    end=dt.microsecond
    print("output {} for {} expected {} took time {}".format(output,a,b,(end-start)))
    assert(output==b)


check([1,8,6,2,5,4,8,3,7], 49 )
check([1,2,3,4,5,4,3,2,1], 12 )



