

from datetime import datetime
from math import floor

verbose=True
def debug(msg):
    if verbose:
        print(msg)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def str_list(l1:ListNode):
    resStr=""
    if l1!=None:
        while(True):
            resStr=resStr+"->"+str(l1.val)
            if(l1.next==None):
                break
            l1=l1.next
    return resStr

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        result=None
        last=None

        while(len(lists)>0):
            minindex=-1
            min=10001
            for i,list in enumerate(lists):
                if list==None:
                  lists.remove(list)
                  minindex=-1
                  break
                else:
                    if list.val<min:
                        min=list.val
                        minindex=i
            if (minindex!=-1):
                element=lists[minindex]
                lists[minindex]=lists[minindex].next
                if result==None:
                    result=element
                    element.next=None
                    last=result
                else:
                    last.next=element
                    last=element
                    element.next=None
        return result

sol=Solution()

def check(a,b):
    dt = datetime.now()
    start=dt.microsecond
    output=sol.mergeKLists(a)
    dt = datetime.now()
    end=dt.microsecond
    print("output {} for {} expected {} took time {}".format(len(output),a,len(b),(end-start)))
    #assert(output==b)


sol=Solution()
l13=ListNode(4,None)
l12=ListNode(3,l13)
l11=ListNode(2,l12)

l23=ListNode(6,None)
l22=ListNode(5,l23)
l21=ListNode(4,l22)


#print("output {} ".format(str_list(sol.mergeKLists([l21,l11]))))
print("output {} ".format(str_list(sol.mergeKLists([l21,l11, None]))))
print("output {} ".format(str_list(sol.mergeKLists([None, None]))))
print("output {} ".format(str_list(sol.mergeKLists([]))))
