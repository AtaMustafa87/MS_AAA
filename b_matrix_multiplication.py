def MatrixMultiplocation(p):
    n = len(p)-1
    m = [[float('inf') for _ in range(n)] for __ in range(n)]
    return LookUpChain(m,p,0,n-1)

def LookUpChain(m,p,i,j):
    if m[i][j] < float('inf'): return m[i][j]
    print('calling for ',i,j)
    if i==j: return 0
    for k in range(i,j):
        q = LookUpChain(m,p,i,k)+LookUpChain(m,p,k+1,j)+ p[i]*p[k+1]*p[j+1]
        if q < m[i][j]:
            m[i][j] = q
    return m[i][j]

print(MatrixMultiplocation([3,4,5,8]))