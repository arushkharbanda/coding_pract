from datetime import  datetime
def check(input,  expected, fn):
    start=datetime.now().microsecond
    output=fn(*input)
    end=datetime.now().microsecond
    print("passed - {}, actual - {}, expected - {}, running time - {}".format(output in expected,output,expected, (end-start)))
