# 10, 20, 3, 4,2
#In sorting algorithm we mark the first element and find out lowest in the reamining arr 
#  and if lowest element in the remaining arr is lower than first element
# then we will swap the 2 elements 
# 1) 2 10 3 4 20  This will put our lowest element in the first position
# In second iteration we will not touch first element as it is already sorted 
#  In the remining elements we will mark first remining element and find the lowest 
#  if the lowest is smaller than first remining elements then we will swap those 2 numbers
# 2) 2 3 10 4 20
# In the third iteration we will not touch the first 2 elements as they are already sorted
# will will then mark the first element from the remaining elements(in this case 10) and
# find out lowest elment and compare it with the first element from the remaining elements and swap if needed
# 3) 2 3 4 10 20
# In the fourth iteration will do the same, not touch the first 3 elements and mark 4th element as first and 
# find out lowest element from the remaining elements and swap if needed
# 4) 2 3 4 10 20

# Time Complexity: O(N*N)

def sorting_algo(arr):
    for i in range(len(arr)-1):
        first = arr[i]
        min_index = arr.index(min(arr[i+1:]),i+1 )
        if arr[min_index] < first :
            arr[i], arr[min_index]  = arr[min_index], arr[i]
    return arr

print(sorting_algo([10, 20, 6, 4, 3, 3, 4]))
print(sorting_algo([5,4,3,2,1]))
print(sorting_algo([5,4,3,10,30,20,40,20,2,1]))

