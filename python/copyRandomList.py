# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:

    def displayRandom(self, head):
        curr=head
        res=""
        while curr!=None:
            if curr.random!=None:
                randomvalue=curr.random.val
            else:
                randomvalue="None"
            res+="{}({})->".format(curr.val, randomvalue)
            curr=curr.next
            #print(res)
        print(res)


    def copyRandomList(self, head):
        old_to_new={}
        curr=head
        curr_new=None
        new_head=None
        while curr!=None:
            new_ele=Node(curr.val)
            # first element in the new list
            if curr_new==None:
                curr_new=new_ele
                new_head=new_ele
                # update dict
                old_to_new[curr]=new_ele
            # cons elements in new list - update current element and move pointer
            else:
                curr_new.next=new_ele
                curr_new=new_ele
                # update dict
                old_to_new[curr]=new_ele
                #print("added pointer from {} to {} in dict".format(curr.val,new_ele.val))

            # move pointer forward
            curr=curr.next
        # traverse new list and place randoms
        curr2=head
        new_curr2=new_head
        while curr2!=None:
            random=curr2.random
            if random in old_to_new.keys():
                newrandom=old_to_new[random]
                new_curr2.random=newrandom

            curr2=curr2.next
            new_curr2=new_curr2.next
        return new_head


n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)

n1.next=n2
n2.next=n3
n3.next=n4

n2.random=n1
n3.random=n4
n4.random=n2

sol=Solution()
sol.displayRandom(n1)
sol.displayRandom(sol.copyRandomList(n1))

