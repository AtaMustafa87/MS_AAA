def editDistance(seq1,seq2):
    m = len(seq1)
    n = len(seq2)
    mat = [[0 for i in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                mat[i][j] = j
            elif j == 0:
                mat[i][j] = i
            elif seq1[j-1] == seq2[i-1]:
                mat[i][j] = mat[i-1][j-1]
            else:
                mat[i][j] = 1 + min(mat[i-1][j-1],mat[i-1][j],mat[i][j-1])
    return mat
s1 = 'saturday'
s2 = 'sunday'
print(editDistance(s1,s2))