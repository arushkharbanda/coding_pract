import heapq
from util import check

class KthLargest:
    def __init__(self, k: int, nums):
        self.k=k
        heapq.heapify(nums)
        self.h=nums
        while(len(self.h)>self.k):
            heapq.heappop(self.h)


    def add(self, val: int):
        if len(self.h)<self.k:
            heapq.heappush(self.h,val)
        elif len(self.h)>=self.k:
            if val>self.h[0]:
                heapq.heappush(self.h,val)
                while(len(self.h)>self.k):
                    heapq.heappop(self.h)
        return self.h[0]


sol=KthLargest(3, [4, 5, 8, 2])

check([3],4,sol.add)
check([5],5,sol.add)
check([10],5,sol.add)
check([9],8,sol.add)
check([4],8,sol.add)


sol=KthLargest(3, [5,-1])

check([2],-1,sol.add)
check([1],1,sol.add)
check([-1],1,sol.add)
check([3],2,sol.add)
check([4],3,sol.add)