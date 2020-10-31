import heapq
from collections import defaultdict
class Item(object):
    def __init__(self, value, index,counter):
        self.value=value
        self.index=index
        self.counter=counter

    def __lt__(self, itm):
        if self.counter==itm.counter:
            return self.index < itm.index
        else:
            return self.counter < itm.counter

class FreqStack(object):

    def __init__(self):
        self.map_counter=defaultdict(lambda :0)
        self.h=[]
        self.i=0


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        self.map_counter[x]-=1
        count=self.map_counter[x]
        self.i-=1
        itm=Item(x, self.i,count)
        heapq.heappush(self.h, itm)

    def pop(self):
        """
        :rtype: int
        """
        item=heapq.heappop(self.h)
        self.map_counter[item.value]+=1
        return item.value



    def print(self):
        """
        :rtype: int
        """
        print("heap {} map {}".format(self.h[0].value,self.map_counter))


stack=FreqStack()
stack.push(5)
stack.print()
stack.push(7)
stack.print()
stack.push(5)
stack.print()
stack.push(7)
stack.print()
stack.push(4)
stack.print()
stack.push(5)
stack.print()
print(stack.pop())#5
stack.print()
print(stack.pop())#7
stack.print()
print(stack.pop())#5
stack.print()
print(stack.pop())#4
stack.print()


