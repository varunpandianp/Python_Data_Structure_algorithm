def findTriplet(arr, n, X):

    count = 0

    for i in range(n):

        for j in range(i + 1, n):

            for k in range(j + 1, n):

                if arr[i] + arr[j] + arr[k] == X:
                    count += 1

    return count

arr = [1, 2, 3, 4, 5]

X = 9

n= len(arr)

result = findTriplet(arr,n,X)

print(result)