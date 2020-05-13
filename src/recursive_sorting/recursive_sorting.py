# TO-DO: complete the helpe function below to merge 2 sorted arrays
import random
testArray = [random.randint(1, 100) for _ in range(6)]
print(f'testArray: {testArray}')
def merge( arrA, arrB ):

    
#     # starting at beginning of `a` and `b`
#     # compare the next value of each
#     # add smallest to `merged_arr`

    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    print(f'array A: {arrA}, array B: {arrB}')
    a_i = 0
    b_i = 0
    for i in range(elements):
            
            if a_i >= len(arrA):
                merged_arr[i] = arrB[b_i]
                b_i += 1
            elif b_i >= len(arrB):
                merged_arr[i] = arrA[a_i]
                a_i += 1
            elif arrA[a_i] <= arrB[b_i]:
                merged_arr[i] = arrA[a_i]
                a_i += 1
            else: arrB[b_i] <= arrA[a_i]:
                merged_arr[i] = arrB[b_i]
                b_i += 1
            
                

   
    print(f'merged_arr: {merged_arr}')
    
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    half = len(arr) // 2
    if len(arr) > 1:
        right = arr[half:]
        left = arr[:half]
        # print(f"right: {right}, left: {left}")
        left = merge_sort(left)
        right = merge_sort(right)
        arr = merge(right, left)

        

    return arr



print(merge_sort(testArray))

#Notes from TK

# def merge_sort( arr ):
#     if len( arr ) > 1: 
#         # recursively call merge_sort() on LHS
#         # recursively call merge_sort() on RHS
#         # merge sorted pieces

# def merge_helper( a, b ):
#     merged_arr = []

#     # starting at beginning of `a` and `b`
#     # compare the next value of each
#     # add smallest to `merged_arr`

#     return merged_arr





















# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
