from util import check
import heapq
class Solution:
    def trap(self, input):
        if len(input)<2:
            return 0
        h=[(-1*hei, i) for i,hei in enumerate(input)]
        heapq.heapify(h)
        no1,no1_i=heapq.heappop(h)
        no2,no2_i=heapq.heappop(h)
        no1=no1*-1
        no2=no2*-1
        left=min(no1_i,no2_i)
        right=max(no1_i,no2_i)
        height=min(no1, no2)
        width=right-left-1
        prefilled_arr=[min(x,height) for x in input[left+1:right]]
        pre_filled_volume=sum(prefilled_arr)
        volume=(height*width)-pre_filled_volume
        return volume+self.trap(input[0:left+1])+self.trap(input[right:])

sol=Solution()
check([[4,2,0,3,2,5]],[9], sol.trap)
check([[0,1,0,2,1,0,1,3,2,1,2,1]],[6], sol.trap)
