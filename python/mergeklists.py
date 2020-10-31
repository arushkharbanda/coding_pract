import heapq
from datetime import datetime
from util import ListNode, str_list

setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val if other !=None else False)
class Solution:
    def mergeKLists(self, lists) -> ListNode:

        lists=[item for item in lists if item!=None]
        heapq.heapify(lists)
        result=ListNode(0)
        curr=result

        while lists:
            min_node=heapq.heappop(lists)
            curr.next=min_node
            curr=min_node
            if min_node.next!=None:
                heapq.heappush(lists,min_node.next)
        return result.next

sol=Solution()


l13=ListNode(4,None)
l12=ListNode(3,l13)
l11=ListNode(2,l12)

l23=ListNode(6,None)
l22=ListNode(5,l23)
l21=ListNode(4,l22)

print("output {} ".format(str_list(sol.mergeKLists([l21,l11]))))
