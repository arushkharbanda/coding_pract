from util import check
from math import floor
class Solution:
    def search(self, nums, target: int) -> int:
        start=0
        end=len(nums)-1
        while True:
            middle=start+floor((end-start)/2)
            if nums[middle]>target:
                end=middle-1
            if nums[middle]<target:
                start=middle+1
            if nums[middle]==target:
                return middle
            if end<start:
                return -1

sol=Solution()
check([[-1,0,3,5,9,12],9], 4, sol.search)
check([[-1,0,3,5,9,12],2], -1, sol.search)
check([[2,5],5], 1, sol.search)
