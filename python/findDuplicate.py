from util import check
import heapq

class Solution:
    def findDuplicates(self, nums):
        if len(nums)==0:
            return []
        heapq.heapify(nums)
        duplicates=[]
        previous=heapq.heappop(nums)
        for i in range(len(nums)):
            ele=heapq.heappop(nums)
            if ele==previous:
                duplicates.append(ele)
            previous=ele
        return duplicates

sol=Solution()
check([[]], [[]], sol.findDuplicates)
check([[4,3,2,7,8,2,3,1]], [[2,3]], sol.findDuplicates)
check([[4,3,2,7,8,2,3,1]], [[2,3]], sol.findDuplicates)
check([[1,	2,	3,	4,	5,	6,	21,	22,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	25,	26,]], [[21,22]], sol.findDuplicates)
