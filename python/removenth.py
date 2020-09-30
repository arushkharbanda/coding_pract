from queue import Queue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class CircularQueue:
    #elements are read from front
    #elements are dropped from front when full
    #elements are added at rear
    def __init__(self, size):
        self.elements=[None] * size
        self.size=size
        self.pointer_front=0
        self.pointer_rear=0
    def add(self, ele):
        self.elements[self.pointer_rear]=ele
        self.pointer_rear=self.pointer_rear+1
        if self.pointer_rear==self.size:
            self.pointer_rear=0
            self.pointer_front=self.pointer_front+1
    def get(self, pos):
        tofetch=self.pointer+pos%(self.size-1)
        return self.elements[tofetch]

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
        q=CircularQueue(n+1)
        list_size=0
        if head!=None:
            node=head
            while(True):
                previous=q.add(node)
                node=node.next
                list_size=list_size+1
                if node==None:
                    break
            if list_size==n:
                nth=head
                head=nth.next

            else:
                nth=q.get(1)
                previous=q.get(0)
                previous.next=nth.next

            del nth

        return head
sol=Solution()
l13=ListNode(3,None)
l12=ListNode(4,l13)
l11=ListNode(2,l12)

l23=ListNode(4,None)
l22=ListNode(6,l23)
l21=ListNode(5,l22)

#243->23, 4
#print("for {}".format(str_list(l11)))
#print("output {} ".format(str_list(sol.removeNthFromEnd(l11,2))))

#564->56, 4
print("for {}".format(str_list(l21)))
print("output {} ".format(str_list(sol.removeNthFromEnd(l21,1))))

l=ListNode(1, None)
#print("for {}".format(str_list(l)))
#print("output {} ".format(str_list(sol.removeNthFromEnd(l,1))))
