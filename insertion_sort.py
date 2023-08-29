# Insertion sort consider first element of list is sorted
# Then compare it with the second element
# If Second element is less than first then swap the elements
# Then consider first 2 elements as sorted and then compre it with 3rd element
# Repeat it till n (length of a list)number of times
# 5,4,3,2,1
# 1) 4, 5, 3, 2, 1
# 2) 3, 4, 5, 2, 1
# 3) 2, 3, 4, 5, 1
# 4) 1, 2, 3, 4, 5

#Time complexity is O(N*N) as we are running the loop N number of times and
#  swapping the elements N number of times

def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i-1
        while(j>=0 and curr< arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = curr
    return arr
print(insertion_sort([10, 20, 6, 4, 3]))
print(insertion_sort([5,4,3,2,1]))
print(insertion_sort([5,4,3,10,30,20,40,20,2,1]))