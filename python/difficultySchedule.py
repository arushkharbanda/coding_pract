from util import check
import math
from collections import deque
class Solution:
    # def difficulty(self, days):
    #     diff=0
    #     for day in days:
    #         diff=diff+max(day)
    #     return diff

    def minDifficulty_stack(self, jobDifficulty, d: int):
        splitup=[jobDifficulty]
        possb=[]
        # generate all possib
        q=deque()
        di=max(jobDifficulty)
        q.append(([jobDifficulty], di))
        min_possib=math.inf
        #min_possib_d={i:math.inf for i in range(1,d+1) }
        while q:
            e, di_old=q.pop()
            # if split is of size d then add it to possb
            #diffi=self.difficulty(e)
            diffi=di_old
            if len(e)==d:
                if diffi<min_possib:
                    #print("difficulty {} picked {} ".format(diffi,e))
                    min_possib=diffi
                continue


            for i,a in enumerate(e):
                if len(a)>1:
                    # make splits and create new arrays
                    for position in range(1,len(a)):
                        sub1,sub2=a[0:position], a[position:]
                        di_new=di_old+max(sub1)+max(sub2)-max(a)
                        if di_new<min_possib:
                            n=e.copy()
                            n.remove(a)
                            n.extend([sub1, sub2])
                            q.append((n,di_new))

        return  -1 if min_possib==math.inf else  min_possib

sol=Solution()
check([[6,5,4,3,2,1], 2],[7], sol.minDifficulty_stack)
check([[9,9,9], 4],[-1], sol.minDifficulty_stack)
check([[1,1,1], 3],[3], sol.minDifficulty_stack)
check([[7,1,7,1,7,1],3],[15], sol.minDifficulty_stack)
check([[11,111,22,222,33,333,44,444], 6],[843], sol.minDifficulty_stack)
check([[3], 1],[3], sol.minDifficulty_stack)
check([[143,446,351,170,117,963,785,76,139,772,452,743,23,767,564,872,922,532,957,945,203,615,843,909,458,320,290,235,174,814,414,669,422,769,781,721,523,94,100,464,484,562,941], 5],[1839], sol.minDifficulty_stack)
check([[186,398,479,206,885,423,805,112,925,656,16,932,740,292,671,360], 4],[1803], sol.minDifficulty_stack)
check([[380,302,102,681,863,676,243,671,651,612,162,561,394,856,601,30,6,257,921,405,716,126,158,476,889,699,668,930,139,164,641,801,480,756,797,915,275,709,161,358,461,938,914,557,121,964,315], 10],[1803], sol.minDifficulty_stack)
