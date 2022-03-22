# Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.

def min_and_max(A, N):
    max_num = min_num = A[0]

    for i in range(1, N):
        if A[i] > max_num:
            max_num = A[i]
        elif A[i] < min_num:
            min_num = A[i]
    
    return(max_num, min_num)

print(min_and_max([5, 0, 11, 34, 7777777, 9], 6))
#Output: (7777777, 0)