from util import check
import heapq
class Solution:
    def kClosest(self, points, K: int) :
        h=[]
        result=[]

        if len(points)==0:
            return []

        #n
        for point in points:
            distance=point[0]*point[0]+point[1]*point[1]
            h.append((distance,point))

        #n
        heapq.heapify(h)

        #k
        for i in range(K):
            ele=heapq.heappop(h)
            result.append(ele[1])

        return result


sol=Solution()
check([[[1,3],[-2,2]],1],[[[-2,2]]],sol.kClosest)
check([[[3,3],[5,-1],[-2,4]],2],[[[3,3],[-2,4]],[[-2,4],[3,3]] ],sol.kClosest)
check([[],2],[[] ],sol.kClosest)
