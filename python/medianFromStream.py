import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lower_arr=[]
        self.higher_arr=[]

    def maxheappush(self, element):
        heapq.heappush(self.lower_arr,-1*element)

    def maxheappop(self):
        return -1*heapq.heappop(self.lower_arr)

    def minheappush(self, element):
        heapq.heappush(self.higher_arr,element)

    def minheappop(self ):
        return heapq.heappop(self.higher_arr)


    def addNum(self, num: int) -> None:
        if len(self.lower_arr)>0:
            if -1*num>self.lower_arr[0]:
                self.maxheappush(num)
            else:
                self.minheappush(num)
        else:
            self.maxheappush(num)


        h=len(self.higher_arr)
        l=len(self.lower_arr)

        diff=l-h
        if diff<-1:
            # h to l
            e=self.minheappop()
            self.maxheappush(e)
        elif diff>1:
            # l to h
            e=self.maxheappop()
            self.minheappush(e)

        print("inserted {} and got {} and {}".format(num, self.lower_arr, self.higher_arr) )
        print("median is {}".format(obj.findMedian()))

    def findMedian(self) -> float:

        h=len(self.higher_arr)
        l=len(self.lower_arr)

        diff=l-h
        if diff==0:
            return (self.lower_arr[0]*-1+self.higher_arr[0])/2
        elif diff==1:
            # from lower
            return self.lower_arr[0]*-1
        elif diff==-1:
            # from higher
            return self.higher_arr[0]

# Your MedianFinder object will be instantiated and called as such:

obj = MedianFinder()
obj.addNum(2)
obj.addNum(3)
obj.addNum(4)
obj.addNum(5)
obj.addNum(3)
obj.addNum(8)
obj.addNum(20)
obj.addNum(0)
print("median is {}".format(obj.findMedian()))
obj.addNum(3)
print("median is {}".format(obj.findMedian()))
obj2 = MedianFinder()
obj2.addNum(-1)
obj2.addNum(-2)
obj2.addNum(-3)
obj2.addNum(-4)
obj2.addNum(-5)
print("median is {}".format(obj2.findMedian()))

