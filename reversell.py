
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def str_list(l1:ListNode):
    resStr=""
    while(True):
        resStr=str(l1.val)+"<-"+resStr
        if(l1.next==None):
            break
        l1=l1.next
    return resStr



class Solution:
    def reverseList(self,head:ListNode):
        old=None
        curr=head
        if head:
            next=head.next
        else:
            return None
        while(True):
            curr.next=old
            old=curr
            curr=next
            if next!=None:
                next=next.next
            if curr==None:
                return old




sol=Solution()
l13=ListNode(3,None)
l12=ListNode(4,l13)
head1=ListNode(2,l12)


l23=ListNode(4,None)
l22=ListNode(6,l23)
head2=ListNode(5,l22)

print(str_list(head1))
print("output {} expected {}".format(str_list(sol.reverseList(head1)),""))
print(str_list(head2))
print("output {} expected {}".format(str_list(sol.reverseList(head2)),""))

head1=ListNode(1)
head1.next=ListNode(8)

head2=ListNode(0)
print(str_list(head1))
print("output {} expected {}".format(str_list(sol.reverseList(head1)),""))
print(str_list(head2))
print("output {} expected {}".format(str_list(sol.reverseList(head2)),""))


head1=ListNode(1)
head1.next=ListNode(0)
head1.next.next=ListNode(0)
head1.next.next.next=ListNode(0)
head1.next.next.next.next=ListNode(0)
head1.next.next.next.next.next=ListNode(0)
head1.next.next.next.next.next.next=ListNode(2)

head2=ListNode(5)
head2.next=ListNode(6)
head2.next.next=ListNode(4)

print(str_list(head1))
print("output {} expected {}".format(str_list(sol.reverseList(head1)),""))
print(str_list(head2))
print("output {} expected {}".format(str_list(sol.reverseList(head2)),""))
