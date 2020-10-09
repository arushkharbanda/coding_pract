from datetime import datetime
from math import floor

#verbose=True
verbose=False
def debug(msg):
    if verbose:
        print(msg)

class Solution:
    def merge(self, intervals):
        # Sort intervals
        intervals=sorted(intervals, key=lambda x:x[0] )

        # iterate over intervals
        previous=[]
        result=[]
        for i,interval in enumerate(intervals):
            #match against previous interval
            if previous==[]:
                previous=interval
                continue

            if interval[0]<=previous[1]:
                    # note: equal is overlap
                    # update previous
                    previous=[previous[0], max(interval[1],previous[1])]
            else:
                # put previous to result
                result.append(previous)
                previous=interval
        if previous!=[]:
            result.append(previous)
        return result


sol=Solution()

def check(input1,expected):
    dt = datetime.now()
    start=dt.microsecond
    output=sol.merge(input1)
    dt = datetime.now()
    end=dt.microsecond
    print("output {} for {} expected {} took time {}".format(output,input1,expected,(end-start)))
    assert(output==expected)


check([[1,3],[2,6],[8,10],[15,18]],[[1,6],[8,10],[15,18]])
check([[1,4],[4,5]], [[1,5]])
check([], [])