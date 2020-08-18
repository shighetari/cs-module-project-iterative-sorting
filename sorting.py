
arr = [99, 98, 4, 0 ,5, 2, 3, 1]

#O(n)
def find_num(arr, target_num):
    for x in arr:
        if x == target_num:
            return x
        return -1

find_num(arr, 99)
#print(find_num(arr, 99))

arr = [4, 98, 99, 0 ,5, 2, 3, 1]
# current_element = 4
# current_idx = 2
# Pseudocode for insertion sort
def insertion_sort(arr):
##  start looping at the second element
    for idx in range(1, len(arr)):
        ## pick up the current element and hold it
        current_element = arr[idx]
        current_idx = idx
        ## while current element is less than its left sibling, swap
        while current_idx> 0 and current_element < arr[current_idx -1]:
        ## copy the left sibling to the right
            arr[current_idx] = arr[current_idx -1]
            ## decrement index
            current_idx -= 1
        ## finally, put our current element down
        arr[current_idx] = current_element
        
insertion_sort(arr)
print(arr)
# time complexity of insertion sort?
# n * (1 + 1 + (n *2) + 1)
# n * 3 (3 + 2n)
# 3n + 2n^2
# O(n + 2n^2)
# O(n^2) -- answer

# arr[i], arr[i - 1] arr[i- 1], arr[i] // this is an alternative way to do this 
