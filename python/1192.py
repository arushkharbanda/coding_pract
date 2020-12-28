from util import check
class Solution:
    def criticalConnections(self, n: int, connections):
        in_dict={i:[] for i in range(n)}
        for i,connection in enumerate(connections):
            a,b=connection
            in_dict[a].append(i)
            in_dict[b].append(i)
        result=set()
        for k in in_dict.keys():
            if len(in_dict[k])==1:
                result.add(in_dict[k][0])

        final=[connections[r] for r in result]
        return final

sol=Solution()
#check([4,  [[0,1],[1,2],[2,0],[1,3]]],[[[1,3]], [[3,1]]],sol.criticalConnections)
#check([6,  [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]],[[]],sol.criticalConnections)
#check([2,  [[0,1]]],[[[1,0]], [[0,1]]],sol.criticalConnections)
#check([3,  [[0, 1], [1, 2], [2, 0]]],[[]],sol.criticalConnections)
#check([5,  [[1, 0], [2, 1], [0, 2], [3, 1], [4, 1]]], [[[1, 3], [1, 4]],[[3, 1], [4, 1]]],sol.criticalConnections)
check([6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]],[[[1,3]],[[3,1]]], sol.criticalConnections)