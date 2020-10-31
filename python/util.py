from datetime import  datetime
def check(input,  expected, fn, running_times=None, intervals=None):
    start_m=datetime.now().microsecond
    output=fn(*input)
    end_m=datetime.now().microsecond
    result={}
    if intervals:

        for i,interval in enumerate(intervals):
            total=0
            start, end=interval
            end_times=running_times[end]
            start_times=running_times[start]
            for j,t in enumerate(end_times):
                running=t-start_times[j]
                total=total+running
            result["{}-{}".format(start, end)]=total

    print("passed - {}, actual - {}, expected - {}, running time - {}, interval-breakup- {}".format(output in expected,output,expected, (end_m-start_m), result))


def debug(str, debug_flag):
    if debug_flag:
        print(str)



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
    return resStr+"->None"
