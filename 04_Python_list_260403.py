number_list = [23, 45, 27, 11, 25, 65, 78]

def getIndex(A, B):
    index = 0
    while index < len(A):
        if A[index] == B:
            break
        index += 1
    return index

def getMax(A):
    max_val = A[0]
    for B in A:
        if B > max_val:
            max_val = B
    return max_val

def getMin(A):
    min_val = A[0]
    for B in A:
        if B < min_val:
            min_val = B
    return min_val

def countGT(A, B):
    C = 0
    for D in A:
        if D > B:
            C += 1
    return C

def sumList(A):
    B = 0
    for C in A:
        B += C
    return B

def swapList(A):
    B = []
    for C in A:
        B.insert(0, C)
    return B

print(getIndex(number_list, 25))
print(getMax(number_list))
print(getMin(number_list))
print(countGT(number_list, 42))
print(sumList(number_list))
print(swapList(number_list))
print(number_list)
