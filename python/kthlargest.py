import heapq
class KthLargest:

    def __init__(self, k: int, nums):
        self.k=k
        heapq.heapify(nums)
        self.h=nums
        #print(self.h)


    def add(self, val: int):
        heapq.heappush(val)

sol=KthLargest(3, [4, 5, 8, 2])
#assert(sol.add(3)==4)
#assert(sol.add(5)==5)
#assert(sol.add(10)==5)
#assert(sol.add(9)==8)
#assert(sol.add(4)==8)


#print("input-{} expected-{} output-{}".format(,[None, 4, 5, 5, 8, 8],))