from datetime import datetime
from math import floor


class Solution:
    def missingNumber(self, nums):
        i=0
        nums.append(-1)
        while(True):

            if i==len(nums):
                break
            if i==nums[i] or nums[i]==-1:
                i=i+1
                continue
            else:
                c=nums[nums[i]]
                nums[nums[i]]=nums[i]
                nums[i]=c

        return [i for i,x in enumerate(nums) if x==-1][0]


sol=Solution()

def check(input1,expected):
    dt = datetime.now()
    start=dt.microsecond
    output=sol.missingNumber(input1)
    dt = datetime.now()
    end=dt.microsecond
    print("output {} for {} expected {} took time {}".format(output,input1,expected,(end-start)))
    assert(output==expected)


check([3,0,1],2)
check([9,6,4,2,3,5,7,0,1], 8)
check([], 0)
