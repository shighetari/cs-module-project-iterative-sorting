# if just searching once, maybe dont sort
# if searching a lot, then maybe go ahead and sort


def linear_search(arr, target):
    # Your code here
    # iterate over the entire array
    for index in range(len(arr)):
    # compare each element with the target
        if arr[index] == target:
        # when you find the target, return index
            return index
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here


    return -1  # not found
