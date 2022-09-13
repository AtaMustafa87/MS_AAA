from ctypes import sizeof


def longestCommonSubSequence(s1,s2):
    seq1 = ' '+s1
    seq2 = ' '+s2
    m = len(seq1)
    n = len(seq2)
    mat = [[0 for _ in range(m)] for __ in range(n)]
    #print(mat[3][1])
    for j in range(1,m):
        for i in range(1,n):
            if seq1[j] == seq2[i]:
                mat[i][j] = mat[i-1][j-1] + 1
            else:
                mat[i][j] = max(mat[i-1][j],mat[i][j-1])
    return mat


print(max(max(longestCommonSubSequence('caabc','aababc'))))