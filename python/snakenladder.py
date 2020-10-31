from util import check
from collections import deque
class Solution:
    def straighten(self, arr):
        x=len(arr)
        result=[]
        arr.reverse()
        for i,a in enumerate(arr):
            if i%2==0:
                result.extend(a)
            else:
                a.reverse()
                result.extend(a)
        return  result

    def snakesAndLadders(self, board):
        intermid=self.straighten(board)
        q=deque()
        size=len(intermid)
        # (distance, index)
        # index is count-1
        q.append((0,0))
        traveresed=[]
        while len(q)>0:
            dis, index=q.popleft()
            for i in range(1,7):
                if index+i <size:
                    if not intermid[index+i]==-1:
                        goto=intermid[index+i]-1
                    else:
                        goto=index+i
                    if goto==size-1:
                        #print(" reached {} from origin via path {}".format(goto,path))
                        return dis+1
                    if goto not in traveresed:
                        traveresed.append(goto)
                        q.append((dis+1,goto))
        return -1



sol=Solution()
check([[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]],[4], sol.snakesAndLadders)
check([[[4,3],[1,2]]],[[1,2,3,4]], sol.straighten)
check([[[-1,-1],[-1,-1]]],[1], sol.snakesAndLadders);
check([[[1,1, 1],[1,1, 1],[1,1, 1]]],[-1], sol.snakesAndLadders);
check([[[1,1,-1],[1,1,1],[-1,1,1]]],[-1], sol.snakesAndLadders);
check([[[-1,-1,19,10,-1],[2,-1,-1,6,-1],[-1,17,-1,19,-1],[25,-1,20,-1,-1],[-1,-1,-1,-1,15]]],[2], sol.snakesAndLadders)
check([[[-1,-1,-1,135,-1,-1,-1,-1,-1,185,-1,-1,-1,-1,105,-1],[-1,-1,92,-1,-1,-1,-1,-1,-1,201,-1,118,-1,-1,183,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,179,-1,-1,-1,-1,-1,-1],[-1,248,-1,-1,-1,-1,-1,-1,-1,119,-1,-1,-1,-1,-1,192],[-1,-1,104,-1,-1,-1,-1,-1,-1,-1,165,-1,-1,206,104,-1],[145,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,229,-1],[-1,-1,75,140,-1,-1,-1,-1,-1,-1,-1,-1,43,-1,34,-1],[-1,-1,-1,-1,-1,-1,169,-1,-1,-1,-1,-1,-1,188,-1,-1],[-1,-1,-1,-1,-1,-1,92,-1,171,-1,-1,-1,-1,-1,-1,66],[-1,-1,-1,126,-1,-1,68,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,109,-1,86,28,228,-1,-1,144,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,59,-1,-1,-1,-1,-1,51,-1,-1,-1,62,-1],[-1,71,-1,-1,-1,63,-1,-1,-1,-1,-1,-1,212,-1,-1,-1],[-1,-1,-1,-1,174,-1,59,-1,-1,-1,-1,-1,-1,133,-1,-1],[-1,-1,62,-1,5,-1,16,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,59,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]],[10], sol.snakesAndLadders)
check([[[-1,-1],[-1,-1]]],[1], sol.snakesAndLadders);