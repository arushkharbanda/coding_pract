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
    # Assuming that nums is not empty
    empty1=False
    empty2=False
    carry=0

    # Pointer to linkedlist
    final=None

    # To Avoid Traversal during insertion
    last=None
    while(True):
        n1=0
        if(l1!=None):
            n1=l1.val
            l1=l1.next
            if(l1==None):
                empty1=True

        n2=0
        if(l2!=None):
            n2=l2.val
            l2=l2.next
            if(l2==None):
                empty2=True

        sum=n1+n2+carry
        if sum==0 and empty2 and empty1:
            break
        carry=int(sum/10)
        n=sum%10
        node=ListNode(n,None)
        if final==None:
            final=node
        else:
            last.next=node
        last=node

    if final!=None:
        return final
    else:
        return ListNode(0, None)

l13=ListNode(3,None)
l12=ListNode(4,l13)
l11=ListNode(2,l12)


l23=ListNode(4,None)
l22=ListNode(6,l23)
l21=ListNode(5,l22)

#342 +465
print("output {} expected {}".format(str_list(addTwoNumbers(l11,l21)),342 +465))


#342 +46
print("output {} expected {}".format(str_list(addTwoNumbers(l11,l22)),342 +46))


#342 +4
print("output {} expected {}".format(str_list(addTwoNumbers(l11,l23)),342 +4))


#34 +465
print("output {} expected {}".format(str_list(addTwoNumbers(l12,l21)),34 +465))


#3 +465
print("output {} expected {}".format(str_list(addTwoNumbers(l13,l21)),3 +465))


#0 +0
print("output {} expected {}".format(str_list(addTwoNumbers(ListNode(0,None),ListNode(0,None))),0 +0))
