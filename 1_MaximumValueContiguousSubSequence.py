#--------------------------------------------------------
'''
    if single element,return it is max
    if two elements find max of two
    if more than two iterate over all of it's sub sequence
'''
# cnt = 0
# def findMaxSubSequence(arr):
#     global cnt
#     n = len(arr)
#     if n == 1: return arr[0]
#     if n == 2: return max(arr[0],arr[1])
#     mv = arr[0]
#     for wl in range(1,n+1):
#         i = 0
#         while i < n-wl+1:
#             cnt =  cnt + 1
#             mv = max(mv,sum(arr[i:i+wl]))
#             print(i,i+wl)
#             i = i + 1
#     return mv
# arr = [9, -3, 4, -1]#, -2, 1, 5, -3]
# print(findMaxSubSequence(arr))
# print(cnt)
def maxSubArraySum(a,size):
    max_so_far =a[0]
    curr_max = a[0]
    # si =0
    # ei = 0
    for i in range(1,size):
        #if a[i] > curr_max + a[i]:
        # if 0 > curr_max: # if current sum is negetive, select current item as maximum value
        #     curr_max = a[i]
        #     si = i
        #     ei = si
        # else:
        #     curr_max = curr_max + a[i]
        #     ei = ei + 1#
        curr_max = max(a[i], curr_max + a[i])# consider next element
        max_so_far = max(max_so_far,curr_max)
    return max_so_far

# Driver function to check the above function
a = [-2, -3, -4]#, -1, -2, 1, 5, -3]
a = [1,2,6,4,3,1,-1]
print("Maximum contiguous sum is" , maxSubArraySum(a,len(a)))

#This code is contributed by _Devesh Agrawal_


