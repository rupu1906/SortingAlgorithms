# Merge Sort is divide and conquer(merge) algorithm

# In this algo we first divide the arr into 2 part adn keep dividing till we get single ele arr
# eg. If we have 9 element arr we will divide it by 2 9//2 => 4 
# [5,4,3,10,30,20,40,20,2]
# [5,4,3,10,30] and [20,40,20,2] then divide it into 2 parts again use numberofele//2
# [5,4,3] [10,30] and [20,40] [20,2] then divide it into 2 parts again use numberofele//2
# [5,4][3] and [10][30] and [20][40] and [20][2]then divide it into 2 parts again use numberofele//2
# # [5][4]and [3] and [10][30] and [20][40] and [20][2]

# Complexity of Divide is O(log N)
# Conquer( Merge)
# [4,5] [3] and [10, 30] and [20,40] and [2,20] -- Merge and sort 
# [3,4,5] and [10,30] and [2,20,20,40] 
# [3,4,5,10,30] and [2,20,20,40]
# [2,3,4,5,10,20,20,30,40]

# Python program for implementation of MergeSort


def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = j= k =0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i]<=right_arr[j]:
                arr[k] = left_arr[i]
                i +=1
            else:
                arr[k] = right_arr[j]
                j +=1
            k +=1
        while i< len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k +=1
        while j< len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr
        
print(merge_sort([6, 5, 12, 10, 9, 1]))
print(merge_sort([6]))
print(merge_sort([]))
print(merge_sort([2,50,3,4,5,10,20,20,30,40,-3,-100,0,-3]))