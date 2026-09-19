def duplicateNumber(arr, n) :
    result =[]

    for i in range(n-2):

        count = 0

        for j in range(n):
            if arr[i] == arr[j]:
                count = count+1

        if count > 1:
            result.append(arr[i])

    return result
arr = [5, 7, 6, 2, 3, 5, 7]

n = len(arr)

result = duplicateNumber(arr, n)

print(result)