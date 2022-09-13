def balancePartition(arr):
    a = []
    b = []
    sumA = 0
    sumB = 0
    if len(arr) < 2: 
        return 'error'
    if len(arr) == 2: 
        return(arr[0],arr[1])
    sa = sorted(arr)
    sa.reverse()
    a.append(sa[0])
    b.append(sa[1])
    sumA = sa[0]
    sumB = sa[1]
    for i in range(2,len(arr)):
        if sumA > sumB:
            b.append(sa[i])
            sumB = sumB + sa[i]
        else:
            a.append(sa[i])
            sumA = sumA + sa[i]
    return(a,b)

arr = [2,7,3,6,8,11]#,2,3]

print(balancePartition(arr))