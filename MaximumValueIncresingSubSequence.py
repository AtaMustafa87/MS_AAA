def findMax(arr):
    max = float('-inf')
    index = -1
    for i,v in enumerate(arr):
        print(i,v)
        if v > max:
            max = v
            index = i
    return (index,max)

def MVCSS(seq):
    # if all of the negatives, then max sequence is max element
    anyPositive = False
    for v in seq:
        if v > 0 :
            anyPositive = True
            break   # some positive value exists
    if not anyPositive:
        print(findMax(seq))
        return
    max = seq[0]
    max_si = 0
    max_ei = 0
    si  = 0
    ei = 0
    sum = seq[0]
    for j in range(1,len(seq)):
        if seq[j] < 0:
            si = j+1
            sum = 0
        else:
            ei = j
            sum = sum + seq[j]
        if sum > max:
            max_si = si
            max_ei = ei
            max = sum
    print(max_si,max_ei,max)

MVCSS([-5,-2,-4,0,-2])