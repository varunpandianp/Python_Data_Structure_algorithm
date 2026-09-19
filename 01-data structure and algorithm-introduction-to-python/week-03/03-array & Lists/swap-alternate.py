# You have been given an array/list(ARR) of size N. You need to swap every pair of alternate elements in the array/list.
#
# You don't need to print or return anything, just change in the input array itself.

def swapAlternate(arr, n):

    for i in range(0, n - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
