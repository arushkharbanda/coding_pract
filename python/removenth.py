from queue import Queue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def str_list(l1:ListNode):
    resStr=""
    if l1!=None:
        while(True):
            resStr=str(l1.val)+"<-"+resStr
            if(l1.next==None):
                break
            l1=l1.next
    return resStr

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast=head
        slow=head
        for i in range(0,n):
            fast=fast.next
        if fast==None:
            head=head.next
            return  head
        while True:
            if fast.next==None:
                slow.next=slow.next.next
                break
            fast=fast.next
            slow=slow.next
        return head


sol=Solution()
l13=ListNode(3,None)
l12=ListNode(4,l13)
l11=ListNode(2,l12)

l23=ListNode(4,None)
l22=ListNode(6,l23)
l21=ListNode(5,l22)

#243->23, 4
print("for {}".format(str_list(l11)))
print("output {} ".format(str_list(sol.removeNthFromEnd(l11,2))))

#564->56, 4
print("for {}".format(str_list(l21)))
print("output {} ".format(str_list(sol.removeNthFromEnd(l21,1))))

l=ListNode(1, None)
print("for {}".format(str_list(l)))
print("output {} ".format(str_list(sol.removeNthFromEnd(l,1))))


head=ListNode(1)
head.next=ListNode(2)
print("for {}".format(str_list(head)))
print("output {} ".format(str_list(sol.removeNthFromEnd(head,2))))
