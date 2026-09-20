def sortZeroesAndOne(arr, n):

    count = 0

    for i in range(n):
        if arr[i] == 0:
            count += 1

    for i in range(count):
        arr[i] = 0

    for i in range(count, n):
        arr[i] = 1

#another approach

def sortZeroesAndOne(arr, n):

    i = 0
    j = n - 1

    while i < j:

        if arr[i] == 0:
            i += 1

        elif arr[j] == 1:
            j -= 1

        else:
            arr[i], arr[j] = arr[j], arr[i]

            i += 1
            j -= 1