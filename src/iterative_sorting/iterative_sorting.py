# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # swapped = True
    # while swapped == True:
        for i in range(len(arr) - 1):
            comparison_done = False
            while comparison_done == False:
                for j in range(i+1, len(arr)):
                    print(f'i: {arr[i]}, j: {arr[j]}')
                    if arr[i] > arr[j]:
                        print()
                        temp = arr[i]
                        print(f'temp: {temp}')
                        arr[i] = arr[j]
                        arr[j] = temp
                        print(f'{arr[i]}, {arr[j]}')
                        comparison_done = True
                    else:
                        comparison_done = True

        print(arr)
        return arr

arr = [3,2,4,7,9,6]
bubble_sort(arr)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr