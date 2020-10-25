from util import check
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        q=deque()
        if root==None:
            return []

        q.append((root,0))
        result={}

        while len(q)>0:
            ele, level=q.popleft()
            if level in result.keys():
                result[level].append(ele.val)
            else:
                result[level]=[ele.val]
            if ele.left!=None:
                q.append((ele.left,level+1))
            if ele.right!=None:
                q.append((ele.right,level+1))
        final=[]
        for level in result.keys():
            elements=result[level]
            if level%2==1:
                elements.reverse()
            final.append(elements)
        return final

ro=TreeNode(3)
l1=TreeNode(9)
r1=TreeNode(20)
rr2=TreeNode(7)
rl2=TreeNode(15)
ro.left=l1
ro.right=r1
r1.right=rr2
r1.left=rl2


sol=Solution()
check([ro],[[[3],[20,9],[15,7]]],sol.zigzagLevelOrder)
check([None],[[]],sol.zigzagLevelOrder)