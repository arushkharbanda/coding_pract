from util import check
from time import sleep
from collections import deque, defaultdict
class Solution:

    def findOrder(self, numCourses: int, prerequisites):
        result=[]
        indegree={x:0 for x in range(numCourses)}
        adjency={i:[] for i in range(numCourses)}
        q=deque()

        for source, target in prerequisites:
            indegree[target]+=1
            adjency[source].append(target)

        q.extend([i for i in range(len(indegree)) if indegree[i]==0])
        while len(q)>0:
            item=q.popleft()
            indegree[item]=-1
            result.insert(0,item)
            children=adjency[item]
            for child in children:
                indegree[child]-=1
                if indegree[child]==0:
                    q.append(child)
        return result if len(result)==numCourses else []

sol=Solution()
# not checking for cycle
check((2, [[1,0]]),[[0,1]],sol.findOrder)
check((4, [[1,0],[2,0],[3,1],[3,2]]),[[0,2,1,3],[0,1,2,3]],sol.findOrder)
check((1, []),[[0]],sol.findOrder)
