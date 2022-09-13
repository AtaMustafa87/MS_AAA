
class Box:
    def __init__(self,w,h,d) -> None:
        self.w = w
        self.h = h
        self.d = d
    
    def __str__(self) -> str:
        return "w = {}, h = {}, d = {}".format(self.w,self.h,self.d)

def getBoxPermutations(box):
    return [Box(box.w,box.h,box.d),Box(box.h,box.d,box.w),Box(box.d,box.w,box.h)]

# generate all of the permutations of the boxes
# concatenate all of box permutations
# sort based on any side say (w)
# find longest increasing sequence for (d) here (h) will be controlling element
#  i.e., in longest increasing sequence check values of 'd' and maintain 'h', instead of adding 1 add 'h'

