from math import floor
# Definition for singly-linked list.
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




def addTwoNumbers(l1:ListNode, l2:ListNode):
    a=0
    ca=0
    cb=0
    while l1:
       a=l1.val*pow(10,ca)+a
       ca=ca+1
       l1=l1.next

    b=0
    while l2:
        b=l2.val*pow(10,cb)+b
        l2=l2.next
        cb=cb+1
    sum=a+b
    final=None
    current=None
    if sum==0:
        return ListNode(0)
    while sum!=0:
        carry=sum%10
        sum=floor(sum/10)
        newNode=ListNode(carry)
        if(final==None):
            final=newNode
            current=final
        else:
            current.next=newNode
            current=newNode
    return final


l13=ListNode(3,None)
l12=ListNode(4,l13)
l11=ListNode(2,l12)


l23=ListNode(4,None)
l22=ListNode(6,l23)
l21=ListNode(5,l22)

#print("output {} expected {}".format(str_list(addTwoNumbers(l11,l21)),342+465))

#81 +0
head1=ListNode(1)
head1.next=ListNode(8)

head2=ListNode(0)
#print("output {} expected {}".format(str_list(addTwoNumbers(head1,head2)),81 +0))



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

print("output {} expected {}".format(str_list(addTwoNumbers(head1,head2)),0))


#342 +4
#print("output {} expected {}".format(str_list(addTwoNumbers(l11,l23)),342 +4))


#34 +465
#print("output {} expected {}".format(str_list(addTwoNumbers(l12,l21)),34 +465))


#3 +465
#print("output {} expected {}".format(str_list(addTwoNumbers(l13,l21)),3 +465))


#0 +0
#print("output {} expected {}".format(str_list(addTwoNumbers(ListNode(0,None),ListNode(0,None))),0 +0))
