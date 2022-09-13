def BottomUpRodCut(p,n):
    r = [0]*(n+1)
    for j in range(1,n+1):
        q = float('-inf')
        for i in range(1,j+1):
            if q < p[i]+r[j-i]:
                q = p[i]+r[j-i]
        r[j] = q
    return (r)

denominations = [0,1, 5, 8, 9, 10, 17, 20, 24, 30]
print(BottomUpRodCut(denominations,5))

