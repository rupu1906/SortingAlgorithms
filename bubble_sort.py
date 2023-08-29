#Bubble sort alogorithm: 
# 10 20 6 4 3 
    # First Iteration
    # 1) We will check first elemenet greter than 2nd element
    #  Will check if 10 is greater than 20 if yes we will swap the 10 and 20 
    # Output: 10 20 6 4 3 
    # 2) Then we will check second elemenet greter than 3rd element
    # will check if 20 is greater than 6 if yes we will swap the 20 with 6
    # Output: 10 6 20 4 3 
    # 3) Then we will check 3rd elemenet greter than 4th element
    # Then we will check if 20 is greater than 4 if yes we will swap the 20 with 4
    # Output: 10 6 4 20 3 
    # 4)Then we will check 4th elemenet greter than 5th element
    # Will check if 20 is greater than 3 if yes we will swap the 20 with 3
    # Output: 10 6 4 3 20 

    # In first iteration we will get the largest number at the last positon

    # Second Iteration
    # Will follow the same steps from iteration one and this will give us the second largest
    # element at second last postion
    # 1) Output: 6 10 4 3 20   
    # 2) Output: 6 4 10 3 20
    # 3) Output: 6 4 3 10 20 

    # Third Iteration
     # Will follow the same steps from iteration one and this will give us the third largest
    # element at third last postion 
    # 1) Output: 4 6 3 10 20   
    # 2) Output: 4 3 6 10 20

    # Fourth Iteration
    # Will follow the same steps from iteration one and this will give us the fourth largest
    # element at fourth last postion 
    # 1) Output: 3 4 6 10 20   


# So logic could be we are running 2 loops
# outer loop runs for length of array-1
# inner loop first runs from 1 till length of array - value of outter for loop

# Time complexity = O(n*n)

def bubble_sort(arr):
    # We are staring for loop from 0 till length of arr -1
    for i in range(len(arr)):
        # We are staring inner for loop from 1 till length of arr - i
        # Reson to start at 1 is to avoid array out of bound exception
        for j in range(1,len(arr)-i):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
    return arr
print(bubble_sort([10, 20, 6, 4, 3]))
print(bubble_sort([5,4,3,2,1]))
print(bubble_sort([5,4,3,10,30,20,40,20,2,1]))

