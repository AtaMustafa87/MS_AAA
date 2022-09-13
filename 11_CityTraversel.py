def calculateDistance(distances,noc):
    ds = [[float('inf') for i in range(noc)] for i in range(noc)]
    ds[0][1] = distances[(0,1)]
    for i in range(1,noc+1):
        ds[0][i] = distances[(i,i)]+ ds[0][i-1]
    for i in range(1,noc+1):
        ds[i][0] = distances[(i,i)]+ ds[i-1][0]
    for i in range(noc+1):
        for j in range(1,noc+1):
            ds[i][j] = min([ds[i-1][j-1]+distances[(i,j)]])
            
    return ds



dis = {
    (1,1):3,
    (2,2):5,
    (3,3):2
}

print(calculateDistance(dis,3))

'''
Given : Ordered Sequence of cities and distances between cities
let A, B & C are cities
distance b/w cities are
d(A,B), d(A,C), d(B,C)
Two persons: X & Y
base Case: Person X travels all of the cities
Iterative Case: Move Persone City A, B, C.... and maintain their cost and store minimum           Person Y travels One City

'''